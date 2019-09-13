# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

# ---- example index page ----
def index():
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'))

# ---- API (example) -----
@auth.requires_login()
def api_get_user_email():
    if not request.env.request_method == 'GET': raise HTTP(403)
    return response.json({'status':'success', 'email':auth.user.email})

# ---- Smart Grid (example) -----
@auth.requires_membership('admin') # can only be accessed by members of admin groupd
def grid():
    response.view = 'generic.html' # use a generic view
    tablename = request.args(0)
    if not tablename in db.tables: raise HTTP(403)
    grid = SQLFORM.smartgrid(db[tablename], args=[tablename], deletable=False, editable=False)
    return dict(grid=grid)

# ---- Embedded wiki (example) ----
def wiki():
    auth.wikimenu() # add the wiki to the menu
    return auth.wiki() 

# ---- Action for login/register/etc (required for auth) -----
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())

# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)

# Cria novo registro no banco
def novo_filme():
    form = SQLFORM(Filmes)
    if form.process().accepted:
        session.flash = 'Novo filme cadastrado: %s' % form.vars.titulo
        redirect(URL('novo_filme'))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    else:
        if not response.flash:
            response.flash = 'Preencha o formulário!'
    return dict(form=form)

# Lista os registro cadastrados no banco
def ver_filmes():
    if request.vars.filme:
        # Busca filme exatamente como está na url e na tabela
        # filmes = db(Filmes.titulo == request.vars.filme).select()

        filmes = db(Filmes.titulo.like('%'+request.vars.filme+'%')).select()
    else:
        filmes = db(Filmes).select()
    return dict(filmes=filmes)

# Atualiza os registro no banco
def editar_filme():
    form = SQLFORM(Filmes, request.args(0, cast=int), showid=False)
    if form.process().accepted:
        session.flash = 'Filme atualizado: %s' % form.vars.titulo
        redirect(URL('ver_filmes'))
    elif form.errors:
        response.flash = 'Erros no formulário!'
    else:
        if not response.flash:
            response.flash = 'Preencha o formulário!'
    return dict(form=form)

# Excluir registro no banco
def apagar_filme():
    db(Filmes.id==request.args(0, cast=int)).delete()
    session.flash = 'Filme apagado!'
    redirect(URL('ver_filmes'))

def teste():
    teste = SQLFORM(db.filmes)

    if teste.process().accepted:
        session.flash = 'hahaha form processado'
        redirect(URL('teste'))
    else:
        response.flash = 'Nao processado'
    return dict(form=teste)