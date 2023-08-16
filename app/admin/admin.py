from flask import Blueprint, current_app
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin, BaseView, expose

from ..extensions import db

from ..models.models import Usuario,Produto,GoogleShopping,Pedido,TreinoProduto

adminbp = Blueprint("views", __name__)

class MyAdminIndexView(AdminIndexView):
    @expose('/')
    def Home(self):
        return self.render('admin/index.html')
    
    
    @expose('/produtopreco')
    def produto(self):
        return self.render('admin/produto_preco.html')

    @expose('/ratingals')
    def als_Rating(self):
        return self.render('admin/view-order.html')
    
    @expose('/classificaproduto')
    def classifica_produto(self):
        return self.render('admin/classifica_produto.html')
    
    @expose('/teste')
    def teste(self):
        
        return self.render('admin/waterfall.html')


admin = Admin(
    current_app,
    name='Admin',
    template_mode='bootstrap3',
    index_view=MyAdminIndexView()
)

current_app.config['FLASK_ADMIN_FLUID_LAYOUT'] = True


'''
   cod_google = db.Column(db.Integer, primary_key=True)
    url_google = db.Column(db.String(100))
    concorrente = db.Column(db.String)
    url_produto = db.Column(db.String)
    cod_produto = db.Column(db.Integer)
    ean = db.Column(db.String)
    preco = db.Column(db.Float)
    custo = db.Column(db.Float)
    margem = db.Column(db.Float)
    statuspreco = db.Column(db.String)
    vendido = db.Column(db.Integer)
    utimavenda = db.Column(db.DateTime)
    precoconcorrente = db.Column(db.Float)
    nomeproduto = db.Column(db.String)
    categoria = db.Column(db.String)
    marca = db.Column(db.String)
    diferencaconcorrente = db.Column(db.Float)
'''
'''
class GoogleShoppingView(ModelView):
    column_searchable_list = ('concorrente', 'url_produto')
    
    
    can_set_page_size = True
    page_size = 15
    create_modal = True
    column_sortable_list = (
        'cod_google', ('cod_google', GoogleShopping.cod_google))
    column_display_pk = True
    column_searchable_list = ['cod_google']
    column_list = ['cod_google',  'ean','nomeproduto',
                   'preco', 'custo', 'margem','concorrente','precoconcorrente']
    column_filters = ['cod_google']
    can_create = True
    can_edit = True
    Can_delete = True
    can_export = True
    column_sortable_list = ('cod_google',)
    column_default_sort = 'cod_google'
    column_details_list = ['preco']
    column_filters = ['preco']
    



class TreinoProdutoView(ModelView):
    can_set_page_size = True
    page_size = 15
    create_modal = True
    column_sortable_list = (
        'cod_treino', ('cod_treino', TreinoProduto.cod_treino))
    column_display_pk = True
    column_searchable_list = ['cod_treino']
    column_list = ['cod_treino', 'titulo', 'categoria', 'cor', 'tamanho',
                   'marca', 'referencia', 'voltagem', 'ambiente',
                   'subcategoria', 'linha', 'tipo', 'imagem', 'Caracteristica']
    column_filters = ['cod_treino']
    can_create = True
    can_edit = True
    can_delete = True
    can_export = True
    column_sortable_list = ('cod_treino',)
    column_default_sort = 'cod_treino'
    column_details_list = ['titulo']
    column_filters = ['titulo']


class ProdutoView(ModelView):
    can_set_page_size = True
    page_size = 15
    create_modal = True
    column_sortable_list = (
        'cod_produto', ('cod_produto',))
    column_display_pk = True
    column_searchable_list = ['cod_produto']
    column_list = ['cod_produto', 'nome', 'marca','preco','concorrente','precoconcorrente',
                   'precosugerido']
    column_filters = ['cod_produto']
    can_view_details = True
    can_create = True
    can_edit = True
    can_delete = True
    can_export = True
    column_display_all_relations = True
    column_sortable_list = ('cod_produto',)
    column_default_sort = 'cod_produto'
    column_details_list = ['cod_produto','preco','urlgoogle','urlanuncio','sugesstaoals','classificacao','precodetalhes']
    column_filters = ['preco']

# Adicione a visualização ao painel administrativo
admin.add_view(ProdutoView(Produtos, db.session))


admin.add_view(GoogleShoppingView(GoogleShopping, db.session))



    
admin.add_view(TreinoProdutoView(TreinoProduto, db.session))

'''





# Define las vistas para cada modelo
admin.add_view(ModelView(Usuario, db.session, category='Comercial', name='Usuarios'))
admin.add_view(ModelView(Produto, db.session, category='Comercial', name='Produtos'))
admin.add_view(ModelView(GoogleShopping, db.session, category='Comercial', name='Google Shopping'))
admin.add_view(ModelView(Pedido, db.session, category='Comercial', name='Pedidos'))
admin.add_view(ModelView(TreinoProduto, db.session, category='Comercial', name='Treino de Produtos'))


