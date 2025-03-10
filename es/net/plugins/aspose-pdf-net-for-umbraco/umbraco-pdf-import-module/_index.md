---
title: Módulo de Importación de PDF de Umbraco
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /es/net/umbraco-pdf-import-module/
description: Aprende cómo instalar y usar el Módulo de Importación de PDF de Umbraco
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Umbraco PDF Import Module",
    "alternativeHeadline": "Umbraco Module Simplifies PDF Content Import Process",
    "abstract": "El Módulo de Importación de PDF de Umbraco permite a los desarrolladores importar contenido PDF sin problemas en sus sitios web de Umbraco sin necesidad de software adicional. Este potente complemento de código abierto simplifica el manejo de documentos al proporcionar una interfaz fácil de usar para obtener y mostrar contenidos PDF al instante, mejorando la eficiencia de la gestión de contenido dentro de aplicaciones .NET",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "950",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/umbraco-pdf-import-module/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/umbraco-pdf-import-module/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

## Introducción

**Aspose.PDF for .NET** es un componente de creación y manipulación de documentos PDF que permite a tus aplicaciones .NET leer, escribir y manipular documentos PDF existentes sin usar Adobe Acrobat. También te permite crear formularios y gestionar campos de formulario incrustados en un documento PDF.

**Aspose.PDF for .NET** es asequible y ofrece una increíble cantidad de características, incluyendo opciones de compresión de PDF; creación y manipulación de tablas; soporte para objetos gráficos; funcionalidad de hipervínculo extensa; controles de seguridad ampliados; manejo de fuentes personalizadas; integración con fuentes de datos; agregar o eliminar marcadores; crear tabla de contenido; agregar, actualizar, eliminar adjuntos y anotaciones; importar o exportar datos de formularios PDF; agregar, reemplazar o eliminar texto e imágenes; dividir, concatenar, extraer o insertar páginas; transformar páginas en imágenes; imprimir documentos PDF y mucho más.

### **Características del Módulo**

La Importación de PDF de Umbraco es un complemento de código abierto de [Aspose](http://www.aspose.com/) que permite a los desarrolladores obtener/leer contenidos de cualquier documento PDF sin requerir ningún otro software. Este complemento demuestra la poderosa función de importación proporcionada por [Aspose.PDF](https://products.aspose.com/pdf/net/). Agrega un control de explorador de archivos simple y un botón de **Importar desde PDF** en la página donde se agrega el complemento. Al hacer clic en el botón, los contenidos del documento se obtienen del archivo y se muestran en la pantalla de inmediato.

## Requisitos del Sistema y Plataformas Soportadas

### **Requisitos del Sistema**

Para configurar el módulo de Importación de PDF de Aspose .NET para Umbraco, necesitas cumplir con los siguientes requisitos:

- Umbraco 6.0+.

No dudes en contactarnos si deseas instalar este módulo en otras versiones de Umbraco.

### **Plataformas Soportadas**

El módulo es compatible con todas las versiones de

- Umbraco que se ejecuta en ASP.NET 4.0.

## Descarga

Puedes descargar Aspose .NET Pdf Import para Umbraco desde una de las siguientes ubicaciones:

- [Github](https://github.com/asposemarketplace/Aspose_for_Umbraco/releases).
- [Sourceforge](https://sourceforge.net/projects/asposeumbraco/files/).
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-umbraco/downloads).
- [Umbraco](https://our.umbraco.com/packages/developer-tools/import-from-pdf-using-asposepdf/).

## Instalación

Una vez descargado, sigue estos pasos para instalar este paquete en tu sitio web de Umbraco:

1. Inicia sesión en la sección **Desarrollador** de Umbraco, por ejemplo <http://www.myblog.com/umbraco/>.
1. Desde el árbol, expande la carpeta **Paquetes**.
   Desde aquí hay dos formas de instalar un paquete: seleccionar **Instalar paquete local** o navegar por el **Repositorio de Paquetes de Umbraco.**.
1. Si instalas **paquete local**, no descomprimas el paquete, sino carga el zip en Umbraco.
1. Sigue las instrucciones en pantalla.

**Nota:** Puedes recibir un error de ‘Longitud máxima de solicitud excedida’ al instalar. Puedes solucionar fácilmente este problema actualizando el valor de ‘maxRequestLength’ en tu archivo web.config de Umbraco.

```xml
  <httpRuntime requestValidationMode="2.0" enableVersionHeader="false" maxRequestLength="25000" />
```

## Uso

Después de haber instalado el macro, es realmente simple comenzar a usarlo en tu sitio web:

1. Asegúrate de estar conectado a la sección **Desarrollador** de Umbraco, por ejemplo <http://www.myblog.com/umbraco/>.
1. Haz clic en **Configuración** en la lista de secciones en la parte inferior izquierda de la pantalla.
1. Expande el nodo **Plantillas** y selecciona la plantilla a la que deseas agregar el macro, por ejemplo, Publicación de blog.
1. Selecciona la posición en la plantilla seleccionada donde deseas el botón.
1. Haz clic en **Insertar Macro** en la cinta superior.
1. Desde **Elegir un macro**, selecciona el macro instalado y haz clic en **OK**.

Has agregado exitosamente la plantilla. Un botón titulado **Importar desde Pdf** ahora aparece en todas las páginas creadas usando esta plantilla. Cualquiera puede simplemente hacer clic en el botón e importar los contenidos de un documento PDF.

## Demostración en Video

Por favor, consulta [el video](https://www.youtube.com/watch?v=zmZTJ86B25E) a continuación para ver el módulo en acción.

## Soporte, Extensión y Contribución

### Soporte

Desde los primeros días de Aspose, supimos que solo ofrecer buenos productos a nuestros clientes no sería suficiente. También necesitábamos brindar un buen servicio. Somos desarrolladores nosotros mismos y entendemos lo frustrante que es cuando un problema técnico o una peculiaridad en el software te impide hacer lo que necesitas hacer. Estamos aquí para resolver problemas, no para crearlos.

Es por eso que ofrecemos soporte gratuito. Cualquiera que use nuestro producto, ya sea que lo haya comprado o esté usando una evaluación, merece nuestra total atención y respeto.

Puedes registrar cualquier problema o sugerencia relacionada con Aspose.PDF .NET para Módulos de Umbraco utilizando cualquiera de las siguientes plataformas:

- [Github](https://github.com/asposemarketplace/Aspose_for_Umbraco/issues).
- [Sourceforge](https://sourceforge.net/p/asposeumbraco/tickets/?source=navbar).
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-umbraco/issues?status=new&status=open).

### Extender y Contribuir

Aspose .NET PDF Import para Umbraco es de código abierto y su código fuente está disponible en los principales sitios web de codificación social que se enumeran a continuación. Se alienta a los desarrolladores a descargar el código fuente y extender la funcionalidad según sus propios requisitos.

#### Código Fuente

Puedes obtener el código fuente más reciente desde una de las siguientes ubicaciones:

- [Github](https://github.com/asposemarketplace/Aspose_for_Umbraco).
- [Sourceforge](https://sourceforge.net/p/asposeumbraco/code/ci/master/tree/).
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-umbraco/src).

#### Cómo configurar el código fuente

Necesitas tener lo siguiente instalado para abrir y extender el código fuente:

- Visual Studio 2010 o superior.

Por favor, sigue estos simples pasos para comenzar:

1. Descarga/Clona el código fuente.
1. Abre Visual Studio 2010 y elige **Archivo** > **Abrir Proyecto**.
1. Navega hasta el código fuente más reciente que has descargado y abre **Aspose.Import from PDF.sln**.