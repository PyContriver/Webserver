from aiohttp import web

routes = web.RouteTableDef()

@routes.get('/home')
async def home(req):
    return web.Response(text="home page")

@routes.get('/users')
async def users(req):
    users = [{'name': 'John Doe', 'email': 'john.doe@example.org'},
            {'name': 'Roger Roe', 'email': 'roger.roe@example.org'}]
    return web.json_response(users)

@routes.get('/users/name')
async def users_name(req):
    return web.Response(text="users name")

@routes.get('/users/names')
async def users_name(req):
    return web.Response(text="users names")

@routes.post('/tasks')
async def tasks(req):
    return web.Response(text="tasks created")

if __name__ == '__main__':
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app, host='localhost', port=12345)
