# Agloe

module.exports = config:
  paths:
    watched: ['agloe']

  plugins:
    autoReload:
      enabled: yes
    coffeelint:
      pattern: /^agloe\/.*\.(coffee)$/
      useCoffeelintJson: yes
    jaded:
      staticPatterns: /^agloe\/markup\/([\d\w]*)\.jade$/
    postcss:
      processors: [
        require('autoprefixer')(['last 8 versions'])
      ]
    stylus:
      plugins: [
        'jeet'
        'bootstrap-styl'
      ]

  npm:
    enabled: yes
    styles:
      'normalize.css': [
        'normalize.css'
      ]

  modules:
    nameCleaner: (path) ->
      path
        .replace /^agloe\//, ''
        .replace /\.coffee/, ''

  files:
    javascripts:
      joinTo:
        'js/libraries.js': /^(?!agloe\/)/
        'js/app.js': /^agloe\//
    stylesheets:
      joinTo:
        'css/libraries.css': /^(?!agloe\/)/
        'css/app.css': /^agloe\//
