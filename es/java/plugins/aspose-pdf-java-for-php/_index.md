---
title: Aspose.PDF Java para PHP
linktitle: Aspose.PDF Java para PHP
type: docs
weight: 50
url: /es/java/aspose-pdf-java-for-php/
description: Aprenda cómo integrar Aspose.PDF for Java en proyectos PHP. Desbloquee funcionalidades avanzadas de PDF para sus aplicaciones web.
lastmod: "2026-09-29"
---
## Introducción a Aspose.PDF Java para PHP

### Puente PHP / Java

El puente PHP/Java es una implementación de streaming, basada en XML\u0412 [protocolo de red](http://php-java-bridge.sourceforge.net/pjb/PROTOCOL.TXT), que se puede usar para conectar un motor de scripts nativo, por ejemplo PHP, Scheme o Python, con una máquina virtual Java. Es hasta 50 veces más rápido que el RPC local a través de SOAP, requiere menos recursos del lado del servidor web. Es [más rápido](http://php-java-bridge.sourceforge.net/pjb/FAQ.html#performance) y más fiable que la comunicación directa a través de la Interfaz Nativa de Java, y no requiere componentes adicionales para invocar procedimientos Java desde PHP o procedimientos PHP desde Java.

Leer más en [sourceforge.net](http://php-java-bridge.sourceforge.net/pjb/)

### Aspose.PDF for Java

Aspose.PDF for Java es un componente de creación de documentos PDF que permite a sus aplicaciones Java leer, escribir y manipular documentos PDF sin usar Adobe Acrobat.

Aspose.PDF for Java es un componente de precio asequible que ofrece una increíble cantidad de características, que incluyen: opciones de compresión de PDF, creación y manipulación de tablas, soporte de gráficos, funciones de imágenes, amplia funcionalidad de hipervínculos, controles de seguridad ampliados y manejo de Font personalizado.

Aspose.PDF for Java le permite crear archivos PDF directamente a través de la API proporcionada y plantillas XML. Usar Aspose.PDF for Java también le permitirá añadir capacidades PDF a sus aplicaciones en poco tiempo.

### Aspose.PDF Java para PHP

El proyecto Aspose.PDF for PHP muestra cómo se pueden realizar diferentes tareas utilizando las APIs de Aspose.PDF Java en PHP. Este proyecto tiene como objetivo proporcionar ejemplos útiles para los desarrolladores PHP que desean utilizar Aspose.PDF for Java en sus proyectos PHP usando [Puente PHP/Java](http://php-java-bridge.sourceforge.net/pjb/).

## Requisitos del sistema y plataformas compatibles

### Requisitos del sistema

A continuación se enumeran los requisitos del sistema para usar Aspose.PDF for PHP via Java:

- Servidor Tomcat 8.0 o superior instalado.
- PHP/JavaBridge está configurado.
- FastCGI está instalado.
- Componente Aspose.PDF descargado.

### Plataformas compatibles

A continuación se presentan las plataformas compatibles:

- PHP 5.3 o superior
- Java 1.8 o superior

## Descargas y configuración

### Descargar bibliotecas requeridas

Descargue las bibliotecas requeridas mencionadas a continuación. Estas son las necesarias para ejecutar ejemplos de Aspose.PDF Java para PHP.

- **Aspose:** [Componente Aspose.PDF for Java](https://downloads.aspose.com/pdf/java)
- Puente PHP/Java

### Descargar ejemplos de sitios de código social

Las siguientes versiones de ejemplos en ejecución están disponibles para descargar en los sitios de código social mencionados a continuación:

### GitHub

- Ejemplos de Aspose.PDF Java para PHP
  - [Aspose.PDF Java para PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)

### Configurar el código fuente en la plataforma Linux

Por favor siga estos pasos simples para abrir y ampliar el código fuente mientras lo utiliza:

### 1. Instalar Tomcat Server

Para instalar el servidor Tomcat, ejecute el siguiente comando en la consola de Linux. Esto instalará correctamente el servidor Tomcat.

{{< highlight actionscript3 >}}

 sudo apt-get install tomcat8

{{< /highlight >}}

### 2. Descargar y configurar PHP/JavaBridge

Para descargar los binarios de PHP/JavaBridge, ejecute el siguiente comando en la consola de Linux.

{{< highlight actionscript3 >}}

  wget http://citylan.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

Descomprima los binarios de PHP/JavaBridge ejecutando el siguiente comando en la consola de Linux.

{{< highlight actionscript3 >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

Esto extraerá **JavaBridge.war** archivo. Cópialo a tomcat88 **webapps** directorio ejecutando el siguiente comando en la consola de Linux.

{{< highlight actionscript3 >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war

{{< /highlight >}}

Al copiar, tomcat8 creará automáticamente una nueva directorio "**JavaBridge**" en **webapps**.

Si aparece algún mensaje de error, entonces instala  **FastCGI** ejecutando el siguiente comando en la consola de Linux.

{{< highlight actionscript3 >}}

  sudo apt-get install php55-cgi

{{< /highlight >}}

Si **JAVA_HOME** error se muestra, entonces abre el archivo /etc/default/tomcat8 y descomenta la línea que establece JAVA_HOME.

### 3. Configurar ejemplos de Aspose.PDF Java para PHP

Clonar, ejemplos PHP ejecutando los siguientes comandos dentro de la directorio webapps/JavaBridge.

{{< highlight actionscript3 >}}

$ git init&nbsp;

$ git clone [https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose.PDF-for-Java_for_PHP]

{{< /highlight >}}

### Configurar el código fuente en la plataforma Windows

Por favor, siga los siguientes pasos simples para configurar PHP/Java Bridge en la plataforma Windows

1. Instale PHP5 y configúrelo como lo hace normalmente.
2. Instale JRE 6 (Java Runtime Environment) si aún no lo tiene. Puede verificar esto en C:\Program Files etc. Puede descargarlo aquí . Yo estoy usando JRE 6 ya que es compatible con PHP Java Bridge (PJB).

3. Instale Apache Tomcat 8.0. Puede descargarlo aquí.

4. Descargue [JavaBridge.war](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/JavaBridgeTemplate621.war/download). Copie este archivo al directorio webapps de tomcat.
(ej: C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps )

5. Reinicie el servicio Apache Tomcat.

6. Vaya a http://localhost:8080/JavaBridge/test.php para comprobar si php funciona. Puede encontrar otros ejemplos allí.

7. Copie su [Aspose.PDF Java](https://downloads.aspose.com/pdf/java) archivo jar a C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib.

8. Clone [Aspose.PDF Java para PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP) ejemplos dentro de la directorio C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\.

9. Copie la directorio C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java a la directorio de ejemplos de Aspose.PDF Java para PHP.

10. Reinicie el servicio Apache Tomcat y comience a usar los ejemplos.

## Soporte, extender y contribuir

### Soporte

Desde los primeros días de Aspose, supimos que simplemente ofrecer a nuestros clientes buenos productos no sería suficiente. También necesitábamos ofrecer un buen servicio. Nosotros también somos desarrolladores y entendemos lo frustrante que es cuando un problema técnico o una peculiaridad del software le impide hacer lo que necesita hacer. Estamos aquí para resolver problemas, no para crearlos.

Esta es la razón por la que ofrecemos soporte gratuito. Cualquier persona que use nuestro producto, ya sea que lo haya comprado o lo esté utilizando en una evaluación, merece toda nuestra atención y respeto.

Puede registrar cualquier problema o sugerencia relacionado con Aspose.Cells Java for PHP usando cualquiera de las siguientes plataformas:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/issues)

### Extender y contribuir

Aspose.PDF Java for PHP es de código abierto y su código fuente está disponible en los principales sitios web de desarrollo colaborativo enumerados a continuación. Se alienta a los desarrolladores a descargar el código fuente y contribuir sugiriendo o añadiendo nuevas funcionalidades o mejorando las existentes, de modo que otros también puedan beneficiarse de él.

### Código fuente

Puede obtener el código fuente más reciente en una de las siguientes ubicaciones

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)
