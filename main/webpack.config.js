const path = require('path');

const HtmlWebpackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const LiveReloadPlugin = require('webpack-livereload-plugin');

// const extractCss = new MiniCssExtractPlugin({filename: "[name].css"});

module.exports = {
    entry: './src/index.js',
    mode: 'development',
    output: {
        path: path.resolve(__dirname, 'static'),
        filename: '[name].bundle.js',
        publicPath: 'static'
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
                test: /\.scss$/,
                exclude: /node_modules/,
                use: [ 'style-loader', 'css-loader', 'postcss-loader', 'sass-loader']
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
