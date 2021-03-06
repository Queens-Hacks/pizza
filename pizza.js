(function() {
  var toppings;

  $.get("scraper/toppings.json", "json")
    .done(function(data) {
      toppings = data;
    })
    .fail(function(xhr) {
      console.error('There was a problem getting the topping map!');
    });

  function getRandomPizza(options) {
    var myPizza = {};
    for (var key in options) {
      var count = options[key];
      myPizza[key] = [];
      for (var i=0; i<count; i++) {
        var choice = Math.floor(Math.random() * toppings[key].length);
        myPizza[key].push(toppings[key][choice]);
      }
    }

    return myPizza;
  }

  function capitalize(string) {
    return string.charAt(0).toUpperCase() + string.substring(1);
  }

  function unpluralize(string) {
    return string.substring(0, string.length - 1);
  }

  function format(string, count) {
    string = capitalize(string);
    if (count === 1) {
      string = unpluralize(string);
    }
    return string;
  }

  $('#options').submit(function(e) {
    e.preventDefault();

    var options = {
      doughs: 1,
      cheeses: 1,
      sauces: 1
    };
    $(e.currentTarget).serializeArray().forEach(function(option) {
      options[option.name] = option.value;
    });

    var pizza = getRandomPizza(options);

    var table = '<h1>Your Pizza!</h1><table class="table">';
    for (var key in pizza) {
      table += '<tr><td style="width: 30%">' + format(key, pizza[key].length) + '</td><td>' + pizza[key].join('<br>') + '</td></tr>';
    }
    table += '</table>';

    $('#result').html(table);
  });
})();
