---
title: Aspose.PDF Java para Jython
linktitle: Aspose.PDF Java para Jython
type: docs
weight: 60
url: /es/java/aspose-pdf-java-for-jython/
description: Combine el poder de Aspose.PDF for Java con Jython. Manipule archivos PDF sin esfuerzo en un entorno Java basado en Python.
lastmod: "2026-09-29"
---
## Introducción

### ¿Qué es Jython?

Jython es una implementación de Python para Java que combina poder expresivo con claridad. Jython está disponible de forma gratuita tanto para uso comercial como no comercial y se distribuye con código fuente. Jython complementa a Java y es especialmente adecuado para las siguientes tareas:

- **Scripting integrado** - Los programadores Java pueden agregar las bibliotecas Jython a su sistema para permitir que los usuarios finales escriban scripts simples o complejos que añadan funcionalidad a la aplicación.
- **Experimentación interactiva** - Jython proporciona un intérprete interactivo que puede usarse para interactuar con paquetes Java o con aplicaciones Java en ejecución. Esto permite a los programadores experimentar y depurar cualquier sistema Java usando Jython.
- **Desarrollo rápido de aplicaciones** - Los programas Python son típicamente de 2 a 10 veces más cortos que el programa Java equivalente. Esto se traduce directamente en una mayor productividad del programador. La interacción fluida entre Python y Java permite a los desarrolladores mezclar libremente los dos lenguajes tanto durante el desarrollo como al lanzar productos.

### Aspose.PDF for Java

Aspose.PDF for Java es un componente de creación de documentos PDF que permite a sus aplicaciones Java leer, escribir y manipular documentos PDF sin usar Adobe Acrobat.

Aspose.PDF for Java es un componente de precio asequible que ofrece una increíble cantidad de funciones, que incluyen: opciones de compresión de PDF, creación y manipulación de tablas, soporte de gráficos, funciones de imagen, amplia funcionalidad de hipervínculos, controles de seguridad ampliados y manejo de fuentes personalizadas.

Aspose.PDF for Java le permite crear archivos PDF directamente mediante la API proporcionada y plantillas XML. Usar Aspose.PDF for Java también le permitirá agregar funcionalidades PDF a sus aplicaciones en poco tiempo.

### Aspose.PDF Java para Jython

Aspose.PDF Java for Jython es un proyecto que muestra / proporciona ejemplos de uso de la API de Aspose.PDF for Java en Jython.

## Requisitos del sistema y plataformas compatibles

### Requisitos del sistema

A continuación se presentan los requisitos del sistema para usar Aspose.PDF Java for Jython:

- Java 1.5 o superior instalado
- Componente Aspose.PDF descargado
- Jython 2.7.0

### Plataformas compatibles

A continuación se presentan las plataformas compatibles:

- Aspose.PDF 15.4 y superiores.
- IDE Java (Eclipse, NetBeans ...)

## Descargar instalación y uso

### Descargar

Las siguientes versiones de ejemplos en ejecución están disponibles para descargar desde GitHub:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose-Pdf-Java-for-Jython)

Descargar componente Aspose.PDF for Java:

- [Aspose.PDF for Java](https://downloads.aspose.com/pdf/java)

### Instalar

- Coloque el archivo jar descargado de Aspose.PDF for Java en el directorio "lib".
- Reemplace "your-lib" con el nombre de archivo jar descargado en el archivo _*init*_.py.

### Utilizar

Puede convertir un documento Pdf a doc utilizando el siguiente código de ejemplo:

```java
from aspose-pdf import Settings
from com.aspose.pdf import Document

class PdfToDoc:

    def __init__(self):
        dataDir = Settings.dataDir + 'WorkingWithDocumentConversion/PdfToDoc/'

        # Open the target document
        pdf = Document(dataDir + 'input1.pdf')

        # Save the concatenated output file (the target document)
        pdf.save(dataDir + "output.doc")

        print "Document has been converted successfully"

if __name__ == '__main__':

    PdfToDoc()
```

## Soporte, extender y contribuir

### Soporte

Desde los primeros días de Aspose, sabíamos que simplemente ofrecer a nuestros clientes buenos productos no sería suficiente. También necesitábamos brindar un buen servicio. Nosotros mismos somos desarrolladores y entendemos lo frustrante que es cuando un problema técnico o una peculiaridad del software le impide hacer lo que necesita. Estamos aquí para resolver problemas, no para crearlos.

Por eso ofrecemos soporte gratuito. Cualquier persona que utilice nuestro producto, ya sea que lo haya comprado o lo esté evaluando, merece toda nuestra atención y respecto.

Puede registrar cualquier problema o sugerencia relacionado con Aspose.PDF Java para Jython utilizando cualquiera de las siguientes plataformas:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/issues)

### Extender y contribuir

Aspose.PDF Java para Jython es de código abierto y su código fuente está disponible en los principales sitios web de desarrollo colaborativo enumerados a continuación. Se anima a los desarrolladores a descargar el código fuente y contribuir sugiriendo o añadiendo nuevas funciones o mejorando las existentes, de modo que otros también puedan beneficiarse de ello.

### Código fuente

Puede obtener el código fuente más reciente de una de las siguientes ubicaciones

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java)
