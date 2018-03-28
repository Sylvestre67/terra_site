const path = require('path');

const HtmlWebpackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const LiveReloadPlugin = require('webpack-livereload-plugin');
const CleanWebpackPlugin = require('clean-webpack-plugin')

const isProd = process.env.NODE_ENV === 'production';

const config = {
    entry: './src/index.js',
    mode: 'development',
    output: {
        path: path.resolve(__dirname, 'static'),
        filename: '[name].bundle.js',
        publicPath: '/static/'
    },
    module: {
        rules: [
            {
                enforce: 'pre',
                test: /\.js?$/,
                use: ['eslint-loader'],
                exclude: /node_modules/
            },
            {
                test: /\.js?$/,
                use: ['babel-loader'],
                exclude: /node_modules/
            },
            {
                test: /\.css$/,
                use: ['style-loader','css-loader', 'postcss-loader']
            },
            {
                test: /\.(png|jpg|gif|svg|eot|otf|ttf|woff|woff2)$/,
                loader: 'url-loader',
                options: {
                    limit: 24
                }
            }
        ]
    },
    plugins: [
        new LiveReloadPlugin(),
        new HtmlWebpackPlugin({
            title: 'Baby Names',
            filename: path.join(__dirname, './templates/base.html'),
            template: path.join(__dirname, './src/index.template.html')
        })
    ]
};


if(isProd){
    const extractCss = new MiniCssExtractPlugin({filename: "[name].[hash].css"});
    const cleanFolder = new CleanWebpackPlugin(['static/*.*']);

    config.output.filename = '[name].[hash].js';
    config.output.publicPath = 'https://storage.googleapis.com/babynames-199117/static/';

    config.mode = 'production';
    config.module.rules[2].use = [MiniCssExtractPlugin.loader, 'css-loader', 'postcss-loader'];

    config.plugins.push(extractCss);
    config.plugins.push(cleanFolder);
}

module.exports = config;