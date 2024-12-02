//BOTÃO PROFILE:
var btnProfile = document.querySelector('#btnProfile');
var profileCard = document.querySelector(".profileCard");


btnProfile.addEventListener('click', function(){
    const displayCardProfile = window.getComputedStyle(profileCard).display;

    if (displayCardProfile === 'none') {
        profileCard.style.display = 'block';
    } else {
        profileCard.style.display = 'none';
    }
});

//-------------------------------------------------------------

//BOTÕES DO CARD LATERAL (SEGUINDO E RECENTES):

var btnRecentes = document.querySelector('#btnRecentes');
var btnSeguindo = document.querySelector('#btnSeguindo');
var containerRecentes = document.querySelector('.containerRecentes');
var containerSeguindo = document.querySelector('.containerSeguindo');

const displayRecentes = window.getComputedStyle(containerRecentes).display;
const displaySeguindo = window.getComputedStyle(containerSeguindo).display;


btnRecentes.addEventListener('click', function() {
    btnRecentes.style.backgroundColor = '#391c50';
    btnSeguindo.style.backgroundColor = '#7334a4';
    if (displaySeguindo === 'block') {
        containerSeguindo.style.display = 'none';
        containerRecentes.style.display = 'block';
    }
}); 

btnSeguindo.addEventListener('click', function(){
    btnSeguindo.style.backgroundColor = '#391c50';
    btnRecentes.style.backgroundColor = '#7334a4';
    if (displayRecentes === 'block') {
        containerRecentes.style.display = 'none';
        containerSeguindo.style.display = 'block';
        containerSeguindo.style.visibility = 'visible';
    }
});

//-------------------------------------------------------------

//BOTÃO - MOSTRAR SENHA
var btnEye = document.querySelector('#btn-eye');
var senhaPerfil = document.querySelector('#senhaPerfil');

btnEye.addEventListener('click', function(){
    if (senhaPerfil.getAttribute('type') == 'password') {
        senhaPerfil.setAttribute('type', 'text');
    } else {
        senhaPerfil.setAttribute('type', 'password');
    }
});
//-------------------------------------------------------------

// BOTÃO - FECHAR CARD ALTERAR FOTO PERFIL e ABRIR CARD ALTERAR FOTO PERFIL
var btnAbrirCardAltFotoPerfil = document.querySelector('#btnAbrirCardAltFotoPerfil');
var cardAlterarFoto = document.querySelector('.alterar-foto');
var btnCloseAltFoto = document.querySelector('#btnCloseAltFoto');

//const displayCardAltFotoPerfil = window.getComputedStyle(cardAlterarFoto).display;

btnAbrirCardAltFotoPerfil.addEventListener('click', function(){
    if (displayCardAltFotoPerfil = window.getComputedStyle(cardAlterarFoto).display === 'none') {
        cardAlterarFoto.style.display = 'grid';
    }
});

btnCloseAltFoto.addEventListener('click', function(){
    if (displayCardAltFotoPerfil = window.getComputedStyle(cardAlterarFoto).display === 'grid'){
        cardAlterarFoto.style.display = 'none';
    }
});
//-------------------------------------------------------------

// BOTÃO - EXCLUIR CONTA


//-------------------------------------------------------------
