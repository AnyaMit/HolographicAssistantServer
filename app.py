import setupenv
setupenv.setup()

import ai
import aimemory
short_term_memory = aimemory.get_memory_redis()
long_term_memory = aimemory.get_vectorstore_azureSearch()
memory = aimemory.get_combined_memory(short_term_memory, long_term_memory)
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

class Dream_Response_Schema(Schema):
    Dreamed = fields.Bool(default=False, description="Did the AI dream?")

class Dream(MethodResource, Resource):
    @doc(description='Enters dream state to persist short term to long term memory', tags=['Dream'])
    @marshal_with(Dream_Response_Schema)
    def post(self, **kwargs):
        return { 'Dreamed': ai.dream(short_term_memory)}

api.add_resource(Dream, '/dream')
docs.register(Dream)

class Packages_Response_Schema(Schema):
    Packages = fields.List(default=[], description="List of Packages", cls_or_instance=fields.String())

class Packages(MethodResource, Resource):
    @doc(description='Lists Packages', tags=['Packages'])
    @marshal_with(Packages_Response_Schema)
    def get(self, **kwargs):
        import pkg_resources
        installed_packages = [(d.project_name, d.version) for d in pkg_resources.working_set]
        return { 'Packages': installed_packages}

api.add_resource(Packages, '/packages')
docs.register(Packages)


if __name__ == '__main__':
   app.run()