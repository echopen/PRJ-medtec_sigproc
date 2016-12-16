var path = require('path');
var express = require('express');

module.exports = function(app) {
    require('./users/route_user')(app);
    require('./settings/route_settings')(app);
    require('./data/route_data')(app);

    app.get('*', function(req, res) {
        res.sendFile(path.resolve('../echopen/client/index.html'));
    });
};