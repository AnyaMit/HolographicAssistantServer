import setupenv
setupenv.setup()

import ai
import aimemory
#memory = aimemory.get_memory_short()
memory = aimemory.get_vectorstore_azureSearch()
agent_chain = ai.get_agent_chain(memory)

from flask import Flask
from flask_restful import Resource, Api
from apispec import APISpec
from marshmallow import Schema, fields
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs
app = Flask(__name__)
api = Api(app)
app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Assistant Server API',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger-json/',  # URI to access API Doc JSON
    'APISPEC_SWAGGER_UI_URL': '/swagger/'  # URI to access UI of API Doc
})
docs = FlaskApiSpec(app)
class Chat_Request_Schema(Schema):
    Prompt = fields.String(required=True, description="Human provided prompt")

class Chat_Response_Schema(Schema):
    Response = fields.String(default='', description="AI generated response")
    Intermediate_Steps = fields.List(fields.String(), default=[], description="AI generated intermediate steps")

class Chat(MethodResource, Resource):
    @doc(description='Returns the response from a human prompt', tags=['Chat'])
    @use_kwargs(Chat_Request_Schema, location=('json'))
    @marshal_with(Chat_Response_Schema)
    def post(self, **kwargs):
        result = ai.get_response(agent_chain, kwargs['Prompt'])
        return {
            'Response': result['output'],
            'Intermediate_Steps': result['intermediate_steps']
                }

api.add_resource(Chat, '/chat')
docs.register(Chat)

if __name__ == '__main__':
   app.run()