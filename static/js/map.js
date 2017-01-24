

    var city = []

city[0] = {
  name: 'Иерусалим',
  lat: 31.783,
  lng: 35.233,
  link: 'https://ru.wikipedia.org/wiki/%D0%98%D0%B5%D1%80%D1%83%D1%81%D0%B0%D0%BB%D0%B8%D0%BC'
};
city[1] = {
  name: 'Тель-Авив',
  lat: 32.083,
  lng: 34.8,
  link: 'https://ru.wikipedia.org/wiki/%D0%A2%D0%B5%D0%BB%D1%8C-%D0%90%D0%B2%D0%B8%D0%B2'
};
city[2] = {
  name: 'Хайфа',
  lat: 32.8,
  lng: 34.983,
  link: 'https://ru.wikipedia.org/wiki/%D0%A5%D0%B0%D0%B9%D1%84%D0%B0'
};
city[3] = {
  name: 'Беэр-Шева',
  lat: 31.258,
  lng: 34.797,
  link: 'https://ru.wikipedia.org/wiki/%D0%91%D0%B5%D1%8D%D1%80-%D0%A8%D0%B5%D0%B2%D0%B0'
};
city[4] = {
  name: 'Арад',
  lat: 31.260,
  lng: 35.214,
  link: 'https://ru.wikipedia.org/wiki/%D0%90%D1%80%D0%B0%D0%B4_(%D0%98%D0%B7%D1%80%D0%B0%D0%B8%D0%BB%D1%8C)'
};
city[5] = {
  name: 'Димона',
  lat: 31.07,
  lng: 35.03,
  link: 'https://ru.wikipedia.org/wiki/%D0%94%D0%B8%D0%BC%D0%BE%D0%BD%D0%B0'
};
city[6] = {
  name: 'Ашкелон',
  lat: 31.665,
  lng: 34.566,
  link: 'https://ru.wikipedia.org/wiki/%D0%90%D1%88%D0%BA%D0%B5%D0%BB%D0%BE%D0%BD'
};
city[7] = {
  name: 'Ашдод',
  lat: 31.797,
  lng: 34.650,
  link: 'https://ru.wikipedia.org/wiki/%D0%90%D1%88%D0%B4%D0%BE%D0%B4'
};
city[8] = {
  name: 'Нетания',
  lat: 32.333,
  lng: 34.85,
  link: 'https://ru.wikipedia.org/wiki/%D0%9D%D0%B5%D1%82%D0%B0%D0%BD%D0%B8%D1%8F'
};
city[9] = {
  name: 'Эйлат',
  lat: 29.55,
  lng: 34.95,
  link: 'https://ru.wikipedia.org/wiki/%D0%AD%D0%B9%D0%BB%D0%B0%D1%82'
};



function initMap() {
    
    var styles = [
      {
        stylers: [
          { hue: "#00ffe6" },
          { saturation: -20 }
        ]
      },{
        featureType: "road",
        elementType: "geometry",
        stylers: [
          { lightness: 100 },
          { visibility: "simplified" }
        ]
      },{
        featureType: "road",
        elementType: "labels",
        stylers: [
          { visibility: "off" }
        ]
      }
    ];

    var map = new google.maps.Map(document.getElementById('map'), {
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        center: {lat: 31.783, lng: 35.233},
        zoom: 7
    });
   
    map.setOptions({styles: styles});
}


$('h3').click(function() {
  
  var index = this.id;
  
  var map = new google.maps.Map(document.getElementById('map'), {
        mapTypeId: google.maps.MapTypeId.HYBRID,
        center: {lat: city[index].lat, lng: city[index].lng},
        zoom: 12
    });
   
    map.setOptions({styles: styles});
    
    
});
            
            
