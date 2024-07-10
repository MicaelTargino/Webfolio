// typing animation
var typed = new Typed('.typing', {
    strings: ['Software Engineer', 'Web developer', 'Data Engineer'],
    typeSpeed: 100,
    backSpeed: 60,
    loop: true
});

var links = $('.nav a.link');
//percorre todos os links contidos em nav
for (i=0;i<links.length;i++) {
    const btn = links[i];
    //quando um botão é clicado, essa função é chamada
    btn.addEventListener('click', (e) => {
        //percorre novamente cada nav link, removendo todas as classes active
        for (p=0;p<5;p++) {
            if (links[p].classList.contains('active')) {
                links[p].classList.remove('active')
            }
        };
        //por fim, adiciona a classe 'active' no link clicado
        e.target.classList.add('active');
        
    });
    //dentro do for mas fora do onclick, esta seção é responsável pelos eventListeners de mouseover e mouseout. quando um botão não tem a classe de ativo, ele está apto para ser manipulado pelo mouseover ou pelo mouseout.
    // if (btn.classList.contains('active') == false) {
        //no mouseover, adiciona uma outra class visando não retirar a classe de um botão que já esteja ativo.
        btn.addEventListener('mouseover', (e) => {
            e.target.classList.add('temporal-active');
        });
        //no mouseout, adiciona uma outra class visando não retirar a classe de um botão que já esteja ativo.
        btn.addEventListener('mouseout', (e) => {
            e.target.classList.remove('temporal-active');
        });
    // }
};

function goToTop() {
    $('.nav a.link').removeClass('active');
    $('.nav a.homeLink').addClass('active');
}

$('#link-topo').click(goToTop);

document.addEventListener('scroll',(e) => {
    const topDistance = window.pageYOffset;
    if (topDistance < 300) {
        document.querySelector('#link-topo').style.bottom = '-3rem';
    }
    if (topDistance > 300) {
        document.querySelector('#link-topo').style.bottom = '3rem';
    }
    if(topDistance < 430){
        removeActive();
        document.querySelector('.homeLink').classList.add('active');
    }
    if(topDistance > 430 && topDistance < 1851){
        removeActive();
        document.querySelector('.aboutLink').classList.add('active');
    }
    if(topDistance > 1851 && topDistance < 2700){
        removeActive();
        document.querySelector('.servicesLink').classList.add('active');
    }
    if(topDistance > 2700 && topDistance < 3466){
        removeActive();
        document.querySelector('.portfolioLink').classList.add('active');
    }
    if(topDistance > 3466 && topDistance < 4300){
        removeActive();
        document.querySelector('.budgetLink').classList.add('active');
    }
    if (topDistance > 4300) { 
        removeActive();
        document.querySelector('.contactBtnLink').classList.add('active');
    }

})

function removeActive() {
    for (p=0;p<6;p++) {
        if (links[p].classList.contains('active')) {
            links[p].classList.remove('active')
        }
    };
};


document.querySelector('#prazo').addEventListener('change', function() {
   const prazo = document.querySelector('#prazo').value
   var semanas = ''
   if(prazo > 1) {
      var semanas = 'weeks'
   } else {
      var semanas = 'week.'
   }
   document.querySelector("label[for=prazo]").innerHTML = `Deadline of ${prazo} ${semanas}`
})
document.querySelector('#deadline').addEventListener('change', function() {
    const prazo = document.querySelector('#deadline').value
    var semanas = ''
    if(prazo > 1) {
       var semanas = 'weeks'
    } else {
       var semanas = 'week.'
    }
    document.querySelector("label[for=deadline]").innerHTML = `Deadline of ${prazo} ${semanas}`
 })

document.querySelector('button#calcularOrcamento').addEventListener('click', (e) => {
    e.preventDefault();
    atualizarPrecoLandingPage();
});
document.querySelector('button#calcularOrcamento2').addEventListener('click', (e) => {
    e.preventDefault();
    atualizarPrecowebApp();
}) 


function atualizarPrecoLandingPage() {
const precoWrapper = document.querySelector('#preco');
const qtde = document.querySelector('#qtde').value;
const prazo = document.querySelector('#prazo').value;
const incluiLayout = document.querySelector('#layout-sim').checked;
const otherFunctionalitys = document.querySelector('input#other-functionalitys').checked;
console.log(otherFunctionalitys);

if (!otherFunctionalitys) {
    var preco = 300;
    if (incluiLayout) {
    preco +=100;
    };
    //quanto menor o prazo, mais o preço aumenta
    if (prazo > 3) {
    var dif = prazo - 3;
    for (k=0; k<dif; k++) {
        preco *= 0.99;
    }
    } else {
    var dif = 3 - prazo;
    for(k=0; k<dif; k++) {
        preco *= 1.15;
    }
} 
document.querySelector('label#preco').innerHTML = `$${(preco/5.3).toFixed(0)} | R$${preco.toFixed(2)}`
} else {
    document.querySelector('label#preco').innerHTML = `<small style="font-size: 13px;">To make a budget with "Other Functionalities", <a href="#contact" style="color:var(--skin-color); text-transform: uppercase; letter-spacing: 0px">Contact me</a></small>`
}

};

function atualizarPrecowebApp() {
    //quantidade de paginas
    var qtde = document.querySelector('input#qtde-pag').value;
    //auth
    var auth = document.querySelector('input#auth').checked;
    // manipular banco de dados
    var bd = document.querySelector('input#bd').checked;
    // atualizações dinâmicas
    var dynamic = document.querySelector('input#dynamic-updates').checked;
    // sistema de busca
    var searchSys = document.querySelector('input#search-system').checked;
    // preciso de um design
    var design = document.querySelector('input#design').checked;
    // prazo
    var deadline = document.querySelector('input#deadline').value;

    var preco;
    preco = qtde * 175;
    if (auth) preco += 120;
    if (bd) preco += 100;
    if (dynamic) preco += 170;
    if (searchSys) preco += 170;
    if (design) preco += 170;
    if (deadline > 7) {
        var dif = deadline -7;
        for(let g=0;g<dif;g++) {
            preco *= 0.98;
        };
    } else if(deadline < 7) {
        var dif = 7 - deadline;
        for(let g=0;g<dif;g++) {
            preco *= 1.05;
        };
    }
    document.querySelector('label#prize').innerHTML = `$${(preco/5.3).toFixed(0)} | R$${preco.toFixed(2)}`
    
};

document.querySelector('button#web-application').addEventListener('click', () => {
    document.querySelector('button#landing-pg').classList.remove('active');
    document.querySelector('button#web-application').classList.add('active');
    document.querySelector('.orcamento-wrapper form#landing-page').style.display = 'none';
    document.querySelector('.orcamento-wrapper form#web-app').style.display = 'flex';
});
document.querySelector('button#landing-pg').addEventListener('click', () => {
    document.querySelector('button#web-application').classList.remove('active');
    document.querySelector('button#landing-pg').classList.add('active');
    document.querySelector('.orcamento-wrapper form#web-app').style.display = 'none';
    document.querySelector('.orcamento-wrapper form#landing-page').style.display = 'flex';  
})