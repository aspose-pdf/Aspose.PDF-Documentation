---
title: Aspose.PDF Java para Jython
type: docs
weight: 60
url: es/java/aspose-pdf-java-for-jython/
lastmod: "2021-06-05"
---

## Introducción

### ¿Qué es Jython?

Jython es una implementación de Python en Java que combina poder expresivo con claridad. Jython está disponible gratuitamente tanto para uso comercial como no comercial y se distribuye con código fuente. Jython es complementario a Java y está especialmente indicado para las siguientes tareas:

- **Scripting embebido** - Los programadores de Java pueden agregar las bibliotecas de Jython a su sistema para permitir que los usuarios finales escriban scripts simples o complicados que agreguen funcionalidad a la aplicación.
- **Experimentación interactiva** - Jython proporciona un intérprete interactivo que se puede usar para interactuar con paquetes de Java o con aplicaciones Java en ejecución. Esto permite a los programadores experimentar y depurar cualquier sistema Java usando Jython.
- **Desarrollo rápido de aplicaciones** - Los programas en Python son típicamente 2-10X más cortos que el programa equivalente en Java.
 Esto se traduce directamente en un aumento de la productividad del programador. La interacción fluida entre Python y Java permite a los desarrolladores mezclar libremente los dos lenguajes tanto durante el desarrollo como en los productos finales.

### Aspose.PDF para Java

Aspose.PDF para Java es un componente de creación de documentos PDF que permite a tus aplicaciones Java leer, escribir y manipular documentos PDF sin usar Adobe Acrobat.

Aspose.PDF para Java es un componente de precio asequible que ofrece una increíble riqueza de características, que incluyen: opciones de compresión de PDF, creación y manipulación de tablas, soporte para gráficos, funciones de imagen, funcionalidad extensa de hipervínculos, controles de seguridad extendidos y manejo de fuentes personalizadas.

Aspose.PDF para Java te permite crear archivos PDF directamente a través del API proporcionado y plantillas XML. Usar Aspose.PDF para Java también te permitirá agregar capacidades PDF a tus aplicaciones en poco tiempo.

### Aspose.PDF Java para Jython

Aspose.PDF Java para Jython es un proyecto que demuestra / proporciona ejemplos de uso del API Aspose.PDF para Java en Jython.
## Requisitos del Sistema y Plataformas Compatibles

### Requisitos del Sistema

Los siguientes son los requisitos del sistema para usar Aspose.PDF Java para Jython:

- Java 1.5 o superior instalado
- Componente Aspose.PDF descargado
- Jython 2.7.0

### Plataformas Compatibles

Las siguientes son las plataformas compatibles:

- Aspose.PDF 15.4 y superior.
- IDE de Java (Eclipse, NetBeans ...)

## Descarga, Instalación y Uso

### Descargando

Las siguientes versiones de ejemplos en ejecución están disponibles para descargar desde GitHub:

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose-Pdf-Java-for-Jython)

Descargue el componente Aspose.PDF para Java:

- [Aspose.PDF para Java](https://downloads.aspose.com/pdf/java)

### Instalando

- Coloque el archivo jar de Aspose.PDF para Java descargado en el directorio "lib".
- Reemplace "your-lib" con el nombre del archivo jar descargado en el archivo _*init*_.py.

### Usando

Puede convertir un documento Pdf a doc usando el siguiente código de ejemplo:

```java
from aspose-pdf import Settings
from com.aspose.pdf import Document

class PdfToDoc:

    def __init__(self):
        dataDir = Settings.dataDir + 'WorkingWithDocumentConversion/PdfToDoc/'


        # Abrir el documento de destino
        pdf = Document(dataDir + 'input1.pdf')

        # Guardar el archivo de salida concatenado (el documento de destino)
        pdf.save(dataDir + "output.doc")

        print "El documento ha sido convertido exitosamente"


if __name__ == '__main__':       

    PdfToDoc()
```


## Soporte, Extender y Contribuir

### Soporte

Desde los primeros días de Aspose, sabíamos que simplemente ofrecer buenos productos a nuestros clientes no sería suficiente. También necesitábamos brindar un buen servicio. Somos desarrolladores y entendemos lo frustrante que es cuando un problema técnico o un fallo en el software te impide hacer lo que necesitas. Estamos aquí para resolver problemas, no para crearlos.

Por eso ofrecemos soporte gratuito. Cualquiera que use nuestro producto, ya sea que lo haya comprado o esté utilizando una versión de evaluación, merece toda nuestra atención y respeto.

Puede registrar cualquier problema o sugerencia relacionada con Aspose.PDF Java para Jython utilizando cualquiera de las siguientes plataformas:

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/issues)

### Extender y Contribuir

Aspose.PDF Java para Jython es de código abierto y su código fuente está disponible en los principales sitios web de codificación social que se enumeran a continuación.
 Developers are encouraged to download the source code and contribute by suggesting or adding new feature or improving the existing ones, so that others could also benefit from it.

Desarrolladores son alentados a descargar el código fuente y contribuir sugiriendo o agregando nuevas funciones o mejorando las existentes, para que otros también puedan beneficiarse de ello.

### Source Code

### Código Fuente

You can get the latest source code from one of the following locations

Puedes obtener el código fuente más reciente de una de las siguientes ubicaciones

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java)