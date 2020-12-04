function ajaxSend(url, params) {
    // Отправляем запрос
    fetch(`${url}?${params}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
    })
        .then(response => response.json())
        .then(json => render(json))
        .catch(error => console.error(error))
}


$('#select-filter').on('change', function() {
  
  var form = $('#filter');
  var data = {}

  data.slug = this.value
  data.name = form.attr("name")

  var url = '/filter/';

  console.log(name)

  let params = new URLSearchParams(data).toString();

  ajaxSend(url, params);
});

function render(data) {
    // Рендер шаблона
    let template = Hogan.compile(html);
    let output = template.render(data);

    const div = document.querySelector('.single-grid-view.tab-pane.fade.in.active.clearfix');
    div.innerHTML = output;
}

let html = '\
{{#queryset}}\
    <div class="col-md-4 col-lg-4 col-sm-4 col-xs-12">\
      <div class="product">\
          <div class="product__inner">\
              <div class="pro__thumb">\
                  <a href="/product/{{ slug }}">\
                      <img src="/media/{{image}}" alt="product images">\
                  </a>\
              </div>\
          </div>\
          <div class="product__details">\
              <h2><a href="/product/{{ slug }}">{{ title }}</a></h2>\
              <ul class="product__price">\
                  <li class="old__price">&#8381;{{ discount_price }}</li>\
                  <li class="new__price">&#8381;{{ price }}</li>\
              </ul>\
          </div>\
      </div>\
  </div>\
{{/queryset}}'
