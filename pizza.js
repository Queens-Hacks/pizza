(function() {
  var toppings = {
    'Cheese': [],
    'Dough': [],
    'Meats': [],
    'Veggies': []
  };

  var types = ['Meats', 'Veggies', 'Dough', 'Cheese'];

  $.get("scraper/toppings.json", "json")
    .done(function(data) {
      data.forEach(function(toppingList, i) {
        toppingList.forEach(function(topping) {
          toppings[types[i]].push(topping);
        });
      });

      console.log(toppings);
    })
    .fail(function(xhr) {
      console.error('There was a problem getting the topping map!');
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
