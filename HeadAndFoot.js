const header = document.querySelector("header");
const footer = document.querySelector("footer");

header.innerHTML=`
<div class="navbarM">
            <nav class="navbar navbar-expand-lg">
                <div class="container-fluid">
                    <a class="logo" href="paginaPrincipal.html">
                        <img src="imagenes/logo2.png" alt="logo" width="150px" height="50px">
                    </a>
                    <button class="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasNavbar" aria-controls="offcanvasNavbar" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarNav">
                        <ul class="nav">
                            <li class="nav-item">
                                <a class="nav-link" href="Catalogo.html">Catálogo</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="Solicitud.html">Solicitud</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="postulacion.html">Postulacion</a>
                            </li>
                        </ul>
                        <form class="d-flex me-3" role="search">
                            <input class="form-control me-2" type="search" placeholder="Buscar" aria-label="Buscar">
                            <button class="btn btn-outline-warning" type="submit"> Buscar </button>
                        </form>
                        <button type="button" class="btnn"> <a class="nav-link" href="Carro.html">Carrito</a> </button>
                        <form>
                            <a href="Registrar.html" class="btn btn-outline-warning" role="button" aria-disabled="true"><i class="bi bi-car-front-fill"> Registrar</i></a>
                        </form>
                    </div>
                </div>
            </nav>
            <div class="offcanvas offcanvas-end" tabindex="-1" id="offcanvasNavbar" aria-labelledby="offcanvasNavbarLabel">
                <div class="offcanvas-header">
                    <h3 class="offcanvas-title" id="offcanvasNavbarLabel"> Menu </h3>
                    <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
                </div>
                <div class="offcanvas-body">
                    <ul class="navbar-nav flex-column">
                        <li class="nav-item">
                            <a class="nav-link" href="paginaPrincipal.html"> Inicio </a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="Catalogo.html">Catálogo</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="Solicitud.html">Solicitud</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav nav-link" data-bs-content="aria-disabled" href="Carro.html"> Carrito</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav nav-link" data-bs-content="aria-disabled" href="postulacion.html"> Postulacion</a>
                        </li>
                    </ul>
                    <form>
                        <a href="Login.html" role="button" aria-disabled="true" class="bi bi-car-front-fill">  Iniciar sesion</a>
                        <span>|</span>
                        <a href="Registrar.html" role="button">Registrar</a>
                    </form>
                </div>
            </div>
        </div>
`;
footer.innerHTML=`
<div class="part-1">
                    <div class="box">
                        <figure>
                            <a href="#">
                                <img src="imagenes/logo2.png" alt="Logo de RM"  >
                            </a>
                        </figure>
                    </div>
                    <div class="box">
                        <h5>Ofertas Exclusivas en tu correo</h5>
                        <input type="text" placeholder="Ingrese su correo">
                        <input type="button" value="Suscribete">
                    </div>
                    <div class="box" id="cont">
                        <h2>Contactanos</h2>
                        <p><i class="bi bi-envelope-at-fill"> tallerrayomakween@gmail.com</i></p>
                        <p><i class="bi bi-telephone-fill"> (+569)7835 6134</i></p>
                    </div>
                </div>
                <div class="part-2">
                    <p>&copy; 2024 <b>Taller Rayo Makween</b> - Todos los Derechos Reservados.</p>
                </div>
`;