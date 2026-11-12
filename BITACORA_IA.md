
# Bitácora de uso de Inteligencia Artificial

## Proyecto: Herramientas en Común

La inteligencia artificial se utilizó como herramienta de apoyo durante el desarrollo del proyecto Django, principalmente para generar ejemplos, organizar componentes y revisar aspectos de seguridad.

Los prompts siguientes resumen las consultas realizadas y no son transcripciones literales.

## 1. Diseño de interfaz

**Prompt representativo:**
¿Cómo puedo estructurar una interfaz HTML sencilla en Django utilizando una plantilla base y páginas que hereden de ella?

**Respuesta de IA:**
Se recomendó utilizar base.html con un menú de navegación y bloques de contenido reutilizables mediante las etiquetas extends y block de Django.

**Aceptado o corregido:**
Se implementó una plantilla base y se organizaron las páginas del proyecto utilizando herencia de templates.

## 2. Estructura del código

**Prompt representativo:**
¿Cómo puedo organizar los modelos Categoria, Herramienta y Prestamo en Django utilizando ForeignKey, PROTECT y estados definidos?

**Respuesta de IA:**
Se proporcionaron ejemplos de modelos relacionados, utilizando campos CharField, BooleanField, DateField y ForeignKey.

**Aceptado o corregido:**
Se incorporó la estructura de los modelos y se comprobó su funcionamiento mediante migraciones y el administrador de Django.

## 3. Revisión de seguridad

**Prompt representativo:**
¿Qué medidas debería revisar para proteger las operaciones de préstamos y evitar que un usuario modifique registros de otros usuarios?

**Respuesta de IA:**
Se recomendaron controles de autenticación, restricciones por permisos, comprobación de propiedad de los préstamos y uso de solicitudes POST para operaciones que modifican datos.

**Aceptado o corregido:**
Se implementaron restricciones de acceso mediante login_required y user_passes_test. También se utilizaron formularios POST con protección CSRF y consultas que limitan la cancelación a los préstamos del usuario conectado.

## Conclusión

La IA se utilizó como apoyo en distintas etapas del proyecto. Se realizaron pruebas de funcionamiento en Django para comprobar las operaciones de herramientas, categorías y solicitudes de préstamo.
