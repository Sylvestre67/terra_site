module.exports = {
    'extends': [
        'prettier',
        'plugin:import/errors',
        'plugin:import/warnings'
    ],
    'plugins': [
        'prettier',
        'import'
    ],
    'parser': 'babel-eslint',
    'parserOptions': {
        'ecmaVersion': 2016,
        'sourceType': 'module'
    },
    'env': {
        'es6': true,
        'browser': true,
        'node': true,
        'jest': true
    },
    'settings': {
        'import/resolver': 'webpack'
    }
};