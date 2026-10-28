# Sistema de Tienda Online de Ropa y Accesorios (E-commerce por Encargo)

## Descripción del Proyecto
Aplicación Web de comercio electrónico desarrollada con Python, Django, Vite.js y Docker, orientada a la exhibición de catálogos de ropa, gestión de carritos de compras y procesamiento de pedidos de prendas personalizadas o a medida.

---

## Metodología de Desarrollo en V (Rama Descendente)

A continuación se detalla la fase de verificación y diseño previa a la codificación del sistema:

### 1. Análisis de Requisitos (Requirement Gathering)
Se determinan las necesidades funcionales del e-commerce y los privilegios de los usuarios:
* Visitante: Explora el catálogo público de prendas, precios, categorías y disponibilidad de tallas.
* Usuario (Cliente): Se registra, inicia sesión, agrega productos al carrito de compras, especifica medidas y realiza pedidos/órdenes de compra.
* Gestor (Ventas/Inventario): Revisa las órdenes entrantes, actualiza el estado de los pedidos (*Pendiente, En Confección, Enviado*) y administra el stock de productos.
* Administrador: Control absoluto de la plataforma, gestión de usuarios, roles y administración de la base de datos desde el panel de Django Admin.

### 2. Análisis del Sistema (System Analysis)
Definición del comportamiento general de la arquitectura cliente-servidor:
* Servicios de Backend: Procesamiento de lógica de negocio, autenticación, gestión del carrito y operaciones transaccionales con Django ORM.
* Servicios de Frontend: Interfaz de usuario dinámica y empaquetado optimizado de recursos mediante Vite.js.
* Persistencia: Almacenamiento relacional para gestionar usuarios, catálogo de ropa, pedidos, detalles de compra y estados de envío.

### 3. Diseño de Software / Arquitectura (Software Design)
Definición del stack tecnológico y aislamiento del entorno:
* Lenguaje y Framework Principal: Python 3.11+ / Django Framework.
* Herramienta de Frontend: Vite.js para la compilación de estilos y scripts modernos.
* Contenedorización: Docker y Docker Compose para garantizar la paridad del entorno de desarrollo y producción.
* Estructura Modular: Apps de Django independientes (autenticacion, productos, pedidos).

### 4. Diseño de Módulos (Module Design)
Especificación de los modelos de datos principales:
* User/Perfil: Roles de usuario (Visitante, Cliente, Gestor, Administrador).
* Producto: Nombre, descripción, precio, categoría, stock e imagen de la prenda.
* Pedido / DetallePedido: Relación de la compra realizada por el cliente, incluyendo cantidad, medidas personalizadas y estado actual del pedido.

---
* Punto de Inflexión: Transición del diseño lógico hacia la construcción e implementación física del código fuente.
---

### 5. Codificación (Coding)
Inicio del desarrollo del código fuente, configurando el entorno en Docker, el backend de Django, el panel administrativo y las rutas del repositorio en GitHub.