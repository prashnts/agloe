# Agloe

{mapStyle} = require './mapstyle'

html2canvas = require 'html2canvas'

App =
  init: ->
    console.log "init success"

  initMap: ->
    map = new google.maps.Map(
      document.getElementById('map'),
        center:
          lat: 28.6139
          lng: 77.2090
        zoom: 15
        styles: mapStyle
    )
    html2canvas '#map'
    # trafficLayer = new google.maps.TrafficLayer()
    # trafficLayer.setMap(map)

module.exports = App
