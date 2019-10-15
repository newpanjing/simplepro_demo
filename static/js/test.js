SIMPLEAPI = {
    init: function (app) {
        console.log(app)
    },
    toolbar: function (type, app) {
        console.log(arguments)
        console.log(this)
        return true;
    }
}