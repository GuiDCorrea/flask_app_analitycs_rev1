
from flask import render_template,jsonify

"""Em caso de erro retorna mensagem amigavel com link de redict"""


def register_handlers(app):
    if app.config.get('DEBUG') is True:
        app.logger.debug('Error Handlers')
        return

    @app.errorhandler(403)
    def forbidden_page(*args, **kwargs):
    
        return jsonify({"forbidden_page":403}),403

    @app.errorhandler(404)
    def page_not_found(*args, **kwargs):
      
        return jsonify({"Pagina nao Encontrada":404}),404
 

    @app.errorhandler(405)
    def method_not_allowed_page(*args, **kwargs):
       
       return jsonify({"method_not_allowed_page":405})
  

    @app.errorhandler(500)
    def server_error_page(*args, **kwargs):
        
        return jsonify({"server_error_page":500}),500