---
title: Aspose.PDF Java para Jython
linktitle: Aspose.PDF Java para Jython
type: docs
weight: 60
url: /es/java/aspose-pdf-java-for-jython/
description: Combine el poder de Aspose.PDF for Java con Jython. Manipule archivos PDF sin esfuerzo en un entorno Java basado en Python.
lastmod: "2026-09-03"
---
## Introducción

### ¿Qué es Jython?

Jython es una implementación de Java de Python que combina poder expresivo con claridad. Jython está disponible de forma gratuita para uso comercial y no comercial y se distribuye con el código fuente. Jython complementa a Java y es especialmente adecuado para las siguientes tareas:

- **Embedded scripting** - Los programadores Java pueden añadir las bibliotecas Jython a su sistema para permitir que los usuarios finales escriban scripts simples o complejos que añadan funcionalidad a la aplicación.
- **Experimentación interactiva** - Jython ofrece un intérprete interactivo que puede usarse para interactuar con paquetes Java o con aplicaciones Java en ejecución. Esto permite a los programadores experimentar y depurar cualquier sistema Java usando Jython.
- **Desarrollo rápido de aplicaciones** - Los programas en Python son típicamente de 2-10X más cortos que el programa Java equivalente. Esto se traduce directamente en una mayor productividad del programador. La interacción fluida entre Python y Java permite a los desarrolladores mezclar libremente los dos lenguajes tanto durante el desarrollo como al entregar productos.

### Aspose.PDF for Java

Aspose.PDF for Java es un componente de creación de documentos PDF que permite a sus aplicaciones Java leer, escribir y manipular documentos PDF sin usar Adobe Acrobat.

Aspose.PDF for Java es un componente de precio accesible que ofrece una increíble cantidad de funciones, entre las que se incluyen: opciones de compresión PDF, creación y manipulación de tablas, soporte de gráficos, funciones de imágenes, funcionalidad extensa de hipervínculos, controles de seguridad ampliados y manejo de Font personalizado.

Aspose.PDF for Java le permite crear archivos PDF directamente a través de la API proporcionada y plantillas XML. Usar Aspose.PDF for Java también le permitirá agregar capacidades PDF a sus aplicaciones en poco tiempo.

### Aspose.PDF Java para Jython

Aspose.PDF Java for Jython es un proyecto que muestra / proporciona ejemplos de uso de la API de Aspose.PDF for Java en Jython.

## Requisitos del sistema y plataformas compatibles

### Requisitos del sistema

A continuación se indican los requisitos del sistema para usar Aspose.PDF Java for Jython:

- Java 1.5 o superior instalado
- Componente Aspose.PDF descargado
- Jython 2.7.0

### Plataformas compatibles

Las siguientes son las plataformas compatibles:

- Aspose.PDF 15.4 y superiores.
- IDE de Java (Eclipse, NetBeans ...)

## Descargar Instalación y Uso

### Descargando

Las siguientes versiones de ejemplos en ejecución están disponibles para descargar desde GitHub:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose-Pdf-Java-for-Jython)

Descargar componente Aspose.PDF for Java:

- [Aspose.PDF for Java](https://downloads.aspose.com/pdf/java)

### Instalando

- Coloque el archivo jar de Aspose.PDF for Java descargado en el directorio "lib".
- Reemplace "your-lib" con el nombre de archivo jar descargado en el archivo _*init*_.py.

### Usando

Puede convertir PDF a documento doc usando el siguiente código de ejemplo:

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

## Apoya, Amplía y Contribuye

### Soporte

Desde los primeros días de Aspose, sabíamos que solo ofrecer a nuestros clientes productos excelentes no sería suficiente. También necesitábamos brindar un buen servicio. Nosotros también somos desarrolladores y entendemos lo frustrante que es cuando un problema técnico o una peculiaridad del software te impide hacer lo que necesitas. Estamos aquí para resolver problemas, no para crearlos.

Por eso ofrecemos soporte gratuito. Cualquier persona que use nuestro producto, ya sea que lo haya comprado o lo esté evaluando, merece toda nuestra atención y respeto.

Puede registrar cualquier problema o sugerencia relacionado conВ Aspose.PDF Java for Jython utilizando cualquiera de las siguientes plataformas:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/issues)

### Extender y Contribuir

Aspose.PDF Java for Jython es de código abierto y su código fuente está disponible en los principales sitios web de desarrollo colaborativo que se enumeran a continuación. Se anima a los desarrolladores a descargar el código fuente y contribuir sugiriendo o añadiendo nuevas funcionalidades o mejorando las existentes, de modo que otros también puedan beneficiarse de ello.

### Código fuente

Puede obtener el código fuente más reciente en una de las siguientes ubicaciones

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java)
