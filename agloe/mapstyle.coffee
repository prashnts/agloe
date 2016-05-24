# Agloe

module.exports =
  mapStyle: [
    {
      'featureType': 'all'
      'elementType': 'all'
      'stylers': [ { 'visibility': 'off' } ]
    }
    {
      'featureType': 'road'
      'elementType': 'geometry'
      'stylers': [
        { 'visibility': 'on' }
        { 'color': '#000000' }
      ]
    }
    {
      'featureType': 'road.arterial'
      'elementType': 'geometry'
      'stylers': [ { 'visibility': 'simplified' } ]
    }
    {
      'featureType': 'road.local'
      'elementType': 'all'
      'stylers': [ { 'visibility': 'off' } ]
    }
  ]
  mapInvisible:[
    {
      "featureType": "all",
      "elementType": "all",
      "stylers": [{"visibility": "off"}]
    }
  ]
