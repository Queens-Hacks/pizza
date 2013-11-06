(function() {
  var toppings = {
    'Cheese': [],
    'Dough': [],
    'Meats': [],
    'Veggies': []
  };

  $.get("https://api.scraperwiki.com/api/1.0/datastore/sqlite?format=jsondict&name=pizza_topping_scraper&query=select%20*%20from%20%60pizzas%60%20order%20by%20'toppingType'", "json")
    .done(function(data) {
      data.forEach(function(topping) {
        toppings[topping.toppingType].push(topping.topping);
      });

      console.log(toppings);
    })
    .fail(function(xhr) {
      console.log('Oh no! it failed!');
    });

  function getRandomPizza(options) {
    var myPizza = {};
    for (key in options) {
      var count = options[key];
      myPizza[key] = [];
      for (var i=0; i<count; i++) {
        var choice = Math.floor(Math.random() * toppings[key].length);
        myPizza[key].push(toppings[key][choice]);
      }
    }

    return myPizza;
  }

  $('#options').submit(function(e) {
    e.preventDefault();

    var options = {};
    $(e.currentTarget).serializeArray().forEach(function(option) {
      options[option.name] = option.value;
    });

    var pizza = getRandomPizza(options);

    var table = '<h1>Your Pizza!</h1><table class="table">';
    for (key in pizza) {
      table += '<tr><td style="width: 30%">' + key + '</td><td>' + pizza[key].join('<br>') + '</td></tr>';
    }
    table += '</table>';

    $('#result').html(table);
  });
})();
