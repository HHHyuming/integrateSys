module.exports = {
    devServer:{
        port: '8888',
        proxy: {
            '/api': {
                target: 'http://192.168.0.103:8000/',
                changeOrigin: true
            }
        }

    }
};