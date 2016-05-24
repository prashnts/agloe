# Agloe
$ = require 'jquery'
{mapStyle, mapInvisible} = require './mapstyle'

App =
  init: ->
    console.log "init success"
    @initEvents()

  initEvents: ->
    ($ 'select[name="map-type"]').on 'change', (e) =>
      mode = ($ e.target).val()

      switch mode
        when 'traffic' then @drawTraffic()
        when 'road' then @drawVisible()
        when 'default' then @drawMap()

  drawVisible: ->
    @drawMap(mapStyle)

  drawTraffic: ->
    @drawMap(mapInvisible)
    trafficLayer = new google.maps.TrafficLayer()
    trafficLayer.setMap @map

  drawMap: (style) ->
    @map = new google.maps.Map(
      document.getElementById('map'),
        center:
          lat: 28.6289143
          lng: 77.2205107
        zoom: 14
        styles: style
    )

module.exports = App
