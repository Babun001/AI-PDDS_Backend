
class apiError extends Error{
    statusCode:number;
    constructor(statusCode:number, msg:string, stack:string){
        super(msg)
        this.statusCode = statusCode
        this.message = msg
        if(stack){
            this.stack = stack;
        }else{
            Error.captureStackTrace(this, this.constructor);
        }
    }
}

export default apiError;