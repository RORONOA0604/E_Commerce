from services.authService import registerService 
async def registerController(data):
    res_obj=await registerService(data)
    return res_obj