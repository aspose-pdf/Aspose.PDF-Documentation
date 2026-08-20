---
title: Aspose.PDF Java para Jython
linktitle: Aspose.PDF Java para Jython
type: docs
weight: 60
url: /java/aspose-pdf-java-for-jython/
description: Combine el poder de Aspose.PDF para Java con Jython. Manipule archivos PDF sin esfuerzo en un entorno Java basado en Python.
lastmod: "2026-06-09"
---
## 
Introducción


### 
¿Qué es Jython?

Jython es una implementación Java de Python que combina poder expresivo con claridad. Jython está disponible gratuitamente para uso comercial y no comercial y se distribuye con el código fuente. Jython es complementario a Java y está especialmente indicado para las siguientes tareas:


- 
**Secuencias de comandos integradas**: los programadores de Java pueden agregar las bibliotecas Jython a su sistema para permitir a los usuarios finales escribir secuencias de comandos simples o complicadas que agreguen funcionalidad a la aplicación.

- 
**Experimentación interactiva**: Jython proporciona un intérprete interactivo que se puede utilizar para interactuar con paquetes Java o con aplicaciones Java en ejecución. Esto permite a los programadores experimentar y depurar cualquier sistema Java utilizando Jython.

- 
**Desarrollo rápido de aplicaciones**: los programas Python suelen ser entre 2 y 10 veces más cortos que el programa Java equivalente. Esto se traduce directamente en una mayor productividad del programador. La perfecta interacción entre Python y Java permite a los desarrolladores mezclar libremente los dos lenguajes tanto durante el desarrollo como en el envío de productos.


### 
Aspose.PDF para Java

Aspose.PDF para Java es un componente de creación de documentos PDF que permite a sus aplicaciones Java leer, escribir y manipular documentos PDF sin utilizar Adobe Acrobat.



Aspose.PDF para Java es un componente de precio asequible que ofrece una increíble riqueza de funciones, que incluyen: opciones de compresión de PDF, creación y manipulación de tablas, compatibilidad con gráficos, funciones de imágenes, amplia funcionalidad de hipervínculos, controles de seguridad ampliados y manejo de fuentes personalizadas.



Aspose.PDF para Java le permite crear archivos PDF directamente a través de las plantillas API y XML proporcionadas. El uso de Aspose.PDF para Java también le permitirá agregar capacidades de PDF a sus aplicaciones en poco tiempo.


### 
Aspose.PDF Java para Jython



Aspose.PDF Java para Jython es un proyecto que demuestra/proporciona ejemplos de uso de la API de Aspose.PDF para Java en Jython.

## Requisitos del sistema y plataformas compatibles


### 
Requisitos del sistema



Los siguientes son los requisitos del sistema para utilizar Aspose.PDF Java para Jython:


- 
Java 1.5 o superior instalado

- 
Componente Aspose.PDF descargado
- Jython 2.7.0


### 
Plataformas compatibles



Las siguientes son las plataformas compatibles:


- 
Aspose.PDF 15.4 y superior.

- 
IDE de Java (Eclipse, NetBeans...)

## Descargar Instalación y Uso


### 
Descargando



Las siguientes versiones de ejemplos en ejecución están disponibles para descargar desde GitHub:


- 
[Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose-Pdf-Java-for-Jython)



Descargue el componente Aspose.PDF para Java:

- [Aspose.PDF para Java](https://downloads.aspose.com/pdf/java)


### 
Instalación


- 
Coloque el archivo jar Aspose.PDF para Java descargado en el directorio "lib".

- 
Reemplace "your-lib" con el nombre del archivo jar descargado en el archivo _*init*_.py.


### 
Usando

Puede convertir un documento PDF a doc utilizando el siguiente código de ejemplo:


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

## 
Apoyar, ampliar y contribuir


### 
Soporte



Desde los primeros días de Aspose, sabíamos que ofrecer a nuestros clientes buenos productos no sería suficiente. También necesitábamos ofrecer un buen servicio. Nosotros mismos somos desarrolladores y entendemos lo frustrante que es cuando un problema técnico o una peculiaridad en el software le impide hacer lo que necesita hacer. Estamos aquí para resolver problemas, no para crearlos.



Es por eso que ofrecemos soporte gratuito. Cualquiera que utilice nuestro producto, ya sea que lo haya comprado o esté utilizando una evaluación, merece toda nuestra atención y respeto.

Puede registrar cualquier problema o sugerencia relacionada con Aspose.PDF Java para Jython utilizando cualquiera de las siguientes plataformas:


- 
[Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/issues)


### 
Ampliar y contribuir



Aspose.PDF Java para Jython es de código abierto y su código fuente está disponible en los principales sitios web de codificación social que se enumeran a continuación. Se anima a los desarrolladores a descargar el código fuente y contribuir sugiriendo o añadiendo nuevas funciones o mejorando las existentes, para que otros también puedan beneficiarse de él.


### 
Código fuente

Puede obtener el código fuente más reciente en una de las siguientes ubicaciones


- 
[Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java)
