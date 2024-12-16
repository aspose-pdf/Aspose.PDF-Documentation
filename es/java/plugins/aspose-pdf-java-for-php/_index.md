---
title: Aspose.PDF Java para PHP
type: docs
weight: 50
url: /es/java/aspose-pdf-java-for-php/
lastmod: "2021-06-05"
---

## Introducción a Aspose.PDF Java para PHP

### PHP / Java Bridge

El PHP/Java Bridge es una implementación de un protocolo de red basado en XML y streaming [protocolo de red](http://php-java-bridge.sourceforge.net/pjb/PROTOCOL.TXT), que puede ser utilizado para conectar un motor de scripts nativo, por ejemplo PHP, Scheme o Python, con una máquina virtual Java. Es hasta 50 veces más rápido que RPC local a través de SOAP, requiere menos recursos en el lado del servidor web. Es [más rápido](http://php-java-bridge.sourceforge.net/pjb/FAQ.html#performance) y más confiable que la comunicación directa a través de la Interfaz Nativa de Java, y no requiere componentes adicionales para invocar procedimientos de Java desde PHP o procedimientos de PHP desde Java.

Lee más en [sourceforge.net](http://php-java-bridge.sourceforge.net/pjb/)

### Aspose.PDF para Java

Aspose.PDF para Java es un componente de creación de documentos PDF que permite a tus aplicaciones Java leer, escribir y manipular documentos PDF sin usar Adobe Acrobat.

Aspose.PDF for Java es un componente a precio asequible que ofrece una increíble cantidad de características, incluyendo: opciones de compresión de PDF, creación y manipulación de tablas, soporte de gráficos, funciones de imágenes, amplia funcionalidad de hipervínculos, controles de seguridad extendidos y manejo de fuentes personalizadas.

Aspose.PDF for Java le permite crear archivos PDF directamente a través del API proporcionado y plantillas XML. Usar Aspose.PDF for Java también le permitirá agregar capacidades PDF a sus aplicaciones en poco tiempo.

### Aspose.PDF Java para PHP

El proyecto Aspose.PDF para PHP muestra cómo se pueden realizar diferentes tareas utilizando las APIs de Aspose.PDF Java en PHP. Este proyecto está diseñado para proporcionar ejemplos útiles para Desarrolladores PHP que desean utilizar Aspose.PDF for Java en sus proyectos PHP usando [PHP/Java Bridge](http://php-java-bridge.sourceforge.net/pjb/).

## Requisitos del Sistema y Plataformas Soportadas

### Requisitos del Sistema

A continuación se presentan los requisitos del sistema para usar Aspose.PDF para PHP a través de Java:

- Tomcat Server 8.0 o superior instalado.
- PHP/JavaBridge está configurado.
- FastCGI está instalado.
- Componente Aspose.PDF descargado.

### Plataformas Compatibles

Las siguientes son las plataformas compatibles:

- PHP 5.3 o superior
- Java 1.8 o superior

## Descargas y Configuración

### Descargar Bibliotecas Requeridas

Descargar las bibliotecas requeridas mencionadas a continuación. Estas son necesarias para ejecutar los ejemplos de Aspose.PDF Java para PHP.

- **Aspose:** [Componente Aspose.PDF para Java](https://downloads.aspose.com/pdf/java)
- PHP/Java Bridge

### Descargar Ejemplos de Sitios de Codificación Social

Las siguientes versiones de ejemplos en ejecución están disponibles para descargar en los sitios de codificación social mencionados a continuación:

### GitHub

- Ejemplos de Aspose.PDF Java para PHP
  - [Aspose.PDF Java para PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)

### Cómo configurar el código fuente en la Plataforma Linux

Por favor, siga estos sencillos pasos para abrir y extender el código fuente mientras utiliza:

### 1. Instalar el Servidor Tomcat

Para instalar el servidor tomcat, emita el siguiente comando en la consola de linux. Esto instalará exitosamente el servidor tomcat.

{{< highlight actionscript3 >}}

 sudo apt-get install tomcat8

{{< /highlight >}}

### 2. Descargar y Configurar PHP/JavaBridge

Para descargar los binarios de PHP/JavaBridge, emita el siguiente comando en la consola de Linux.

{{< highlight actionscript3 >}}

  wget http://citylan.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

Descomprima los binarios de PHP/JavaBridge emitiendo el siguiente comando en la consola de Linux.

{{< highlight actionscript3 >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}


Esto extraerá el archivo **JavaBridge.war**. Cópielo a la carpeta **webapps** de tomcat88 emitiendo el siguiente comando en la consola de Linux.

{{< highlight actionscript3 >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war

{{< /highlight >}}

Al copiar, tomcat8 creará automáticamente una nueva carpeta "**JavaBridge**" en **webapps**.


Si aparece algún mensaje de error, instale **FastCGI** emitiendo el siguiente comando en la consola de Linux.

{{< highlight actionscript3 >}}

  sudo apt-get install php55-cgi

{{< /highlight >}}


Si se muestra un error de **JAVA_HOME**, entonces abre el archivo /etc/default/tomcat8 y descomenta la línea que establece el JAVA_HOME.

### 3. Configurar Aspose.PDF Java para ejemplos en PHP

Clona los ejemplos de PHP emitiendo los siguientes comandos dentro de la carpeta webapps/JavaBridge.

{{< highlight actionscript3 >}}

$ git init&nbsp;

$ git clone [https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose.PDF-for-Java_for_PHP]

{{< /highlight >}}

### Cómo configurar el código fuente en la plataforma Windows

Por favor, sigue los sencillos pasos a continuación para configurar PHP/Java Bridge en la plataforma Windows

1. Instala PHP5 y configúralo como normalmente lo haces.
2. Instala JRE 6 (Entorno de Ejecución de Java) si aún no lo tienes. Puedes verificar esto en C:\Program Files etc. Puedes descargarlo aquí. Estoy usando JRE 6 ya que es compatible con PHP Java Bridge (PJB).

3. Instala Apache Tomcat 8.0. Puedes descargarlo aquí.

4. Descarga [JavaBridge.war](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/JavaBridgeTemplate621.war/download). Copia este archivo al directorio webapps de tomcat.  
(ej: C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps)

5. Reinicia el servicio de apache tomcat.

6. Ve a http://localhost:8080/JavaBridge/test.php para verificar si php funciona. Puedes encontrar otros ejemplos allí.

7. Copia tu archivo jar de [Aspose.PDF Java](https://downloads.aspose.com/pdf/java) a C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib

8. Clona los ejemplos de [Aspose.PDF Java for PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP) dentro de la carpeta C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\.

9. Copia la carpeta C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java a tu carpeta de ejemplos de Aspose.PDF Java for PHP.

10. Reinicia el servicio de apache tomcat y comienza a usar los ejemplos.

## Soporte, Extiende y Contribuye

### Soporte

Desde los primeros días de Aspose, sabíamos que solo darles a nuestros clientes buenos productos no sería suficiente. También necesitábamos ofrecer un buen servicio. Somos desarrolladores y entendemos lo frustrante que es cuando un problema técnico o una peculiaridad en el software te impide hacer lo que necesitas. Estamos aquí para resolver problemas, no para crearlos.

Por eso ofrecemos soporte gratuito. Cualquiera que use nuestro producto, ya sea que lo haya comprado o esté usando una evaluación, merece toda nuestra atención y respeto.

Puede registrar cualquier problema o sugerencia relacionada con Aspose.Cells Java para PHP utilizando cualquiera de las siguientes plataformas:

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/issues)

### Ampliar y Contribuir

Aspose.PDF Java para PHP es de código abierto y su código fuente está disponible en los principales sitios web de codificación social enumerados a continuación.
 Desarrolladores son alentados a descargar el código fuente y contribuir sugiriendo o agregando nuevas características o mejorando las existentes, para que otros también puedan beneficiarse de ello.

### Código Fuente

Puedes obtener el código fuente más reciente de una de las siguientes ubicaciones

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)