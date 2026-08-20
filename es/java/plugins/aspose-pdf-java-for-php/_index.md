---
title: Aspose.PDF Java para PHP
linktitle: Aspose.PDF Java para PHP
type: docs
weight: 50
url: /java/aspose-pdf-java-for-php/
description: Aprenda cómo integrar Aspose.PDF para Java en proyectos PHP. Desbloquee la funcionalidad avanzada de PDF para sus aplicaciones web.
lastmod: "2026-06-09"
---
## 
Introducción a Aspose.PDF Java para PHP


### 
Puente PHP/Java

PHP/Java Bridge es una implementación de un [protocolo de red](http://php-java-bridge.sourceforge.net/pjb/PROTOCOL.TXT) basado en XML, que se puede utilizar para conectar un motor de script nativo, por ejemplo PHP, Scheme o Python, con una máquina virtual Java. Es hasta 50 veces más rápido que RPC local a través de SOAP y requiere menos recursos en el lado del servidor web. Es [más rápido](http://php-java-bridge.sourceforge.net/pjb/FAQ.html#performance) y más confiable que la comunicación directa a través de la interfaz nativa de Java, y no requiere componentes adicionales para invocar procedimientos Java desde PHP o procedimientos PHP desde Java.



Lea más en [sourceforge.net](http://php-java-bridge.sourceforge.net/pjb/)


### 
Aspose.PDF para Java



Aspose.PDF para Java es un componente de creación de documentos PDF que permite a sus aplicaciones Java leer, escribir y manipular documentos PDF sin utilizar Adobe Acrobat.



Aspose.PDF para Java es un componente de precio asequible que ofrece una increíble riqueza de funciones, que incluyen: opciones de compresión de PDF, creación y manipulación de tablas, compatibilidad con gráficos, funciones de imágenes, amplia funcionalidad de hipervínculos, controles de seguridad ampliados y manejo de fuentes personalizadas.

Aspose.PDF para Java le permite crear archivos PDF directamente a través de las plantillas API y XML proporcionadas. El uso de Aspose.PDF para Java también le permitirá agregar capacidades de PDF a sus aplicaciones en poco tiempo.


### 
Aspose.PDF Java para PHP



El proyecto Aspose.PDF para PHP muestra cómo se pueden realizar diferentes tareas utilizando las API Java de Aspose.PDF en PHP. Este proyecto tiene como objetivo proporcionar ejemplos útiles para los desarrolladores de PHP que desean utilizar Aspose.PDF para Java en sus proyectos PHP utilizando [PHP/Java Bridge](http://php-java-bridge.sourceforge.net/pjb/).


## 
Requisitos del sistema y plataformas compatibles


### 
Requisitos del sistema

Los siguientes son los requisitos del sistema para usar Aspose.PDF para PHP a través de Java:


- 
Tomcat Server 8.0 o superior instalado.

- 
PHP/JavaBridge está configurado.

- 
FastCGI está instalado.

- 
Componente Aspose.PDF descargado.

### Plataformas compatibles



Las siguientes son las plataformas compatibles:


- 
PHP 5.3 o superior

- 
Java 1.8 o superior


## 
Descargas y configuración

### Descargar bibliotecas requeridas



Descargue las bibliotecas requeridas que se mencionan a continuación. Estos son los ejemplos necesarios para ejecutar Aspose.PDF Java para PHP.


- 
**Aspose:** [Aspose.PDF para componente Java](https://downloads.aspose.com/pdf/java)

- 
Puente PHP/Java


### 
Descargar ejemplos de sitios de codificación social

Las siguientes versiones de ejemplos en ejecución están disponibles para descargar en los sitios de codificación social que se mencionan a continuación:


### 
GitHub


- 
Aspose.PDF Ejemplos de Java para PHP

  - 
[Aspose.PDF Java para PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)


### 
Cómo configurar el código fuente en la plataforma Linux

Siga estos sencillos pasos para abrir y ampliar el código fuente mientras usa:


### 
1. Instale el servidor Tomcat



Para instalar el servidor Tomcat, ejecute el siguiente comando en la consola de Linux. Esto instalará correctamente el servidor Tomcat.


{{< highlight actionscript3 >}}

 
sudo apt-get instalar tomcat8


{{< /highlight >}}

### 
2. Descargue y configure PHP/JavaBridge

Para descargar los archivos binarios de PHP/JavaBridge, ejecute el siguiente comando en la consola de Linux.


{{< highlight actionscript3 >}}

  
wgethttp://citylan.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip


{{< /highlight >}}


Descomprima los archivos binarios de PHP/JavaBridge emitiendo el siguiente comando en la consola de Linux.


{{< highlight actionscript3 >}}

  
descomprimir -d php-java-bridge_6.2.1_documentation.zip


{{< /highlight >}}


Esto extraerá el archivo **JavaBridge.war**В. Cópielo en la carpeta tomcat88 **webapps**В emitiendo el siguiente comando en la consola de Linux.

{{< highlight actionscript3 >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war


{{< /highlight >}}


Al copiar, Tomcat8 creará automáticamente una nueva carpeta "**JavaBridge**" en **webapps**.



Si aparece algún mensaje de error, instale **FastCGI**В emitiendo el siguiente comando en la consola de Linux.


{{< highlight actionscript3 >}}

  
sudo apt-get instalar php55-cgi


{{< /highlight >}}


Si se muestra el error **JAVA_HOME**В, abra el archivo /etc/default/tomcat8 y descomente la línea que establece JAVA_HOME.

### 3. Configurar Aspose.PDF Java para ejemplos de PHP



Clone ejemplos de PHP emitiendo los siguientes comandos dentro de la carpeta webapps/JavaBridge.


{{< highlight actionscript3 >}}


$ git init



$ git clon [https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose.PDF-for-Java_for_PHP]


{{< /highlight >}}

### 
Cómo configurar el código fuente en la plataforma Windows

Siga los sencillos pasos a continuación para configurar PHP/Java Bridge en la plataforma Windows


1. 
Instale PHP5 y configúrelo como lo hace normalmente

2. 
Instale JRE 6 (Java Runtime Environment) si aún no lo tiene. Puede verificar esto en C:\Program Archivos, etc. Puede descargarlo aquí. Estoy usando JRE 6 porque es compatible con PHP Java Bridge (PJB).


3. 
Instale Apache Tomcat 8.0. Puedes descargarlo aquí


4. 
Descargue [JavaBridge.war](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/JavaBridgeTemplate621.war/download). Copie este archivo al directorio de aplicaciones web de Tomcat.
(por ejemplo: C:\Program Archivos\Apache Software Foundation\Tomcat 8.0\webapps)


5. 
Reinicie el servicio Tomcat Apache.


6. 
Vaya a http://localhost:8080/JavaBridge/test.php para comprobar si php funciona. Puedes encontrar otros ejemplos allí.


7. 
Copie su archivo jar [Aspose.PDF Java](https://downloads.aspose.com/pdf/java) a C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib


8. 
Clonar ejemplos de [Aspose.PDF Java para PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP) dentro de la carpeta C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\.

9. Copie la carpeta C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java a su carpeta de ejemplos Aspose.PDF Java para PHP.


10. 
Reinicie el servicio Apache Tomcat y comience a usar ejemplos.


## 
Apoyar, ampliar y contribuir


### 
Soporte



Desde los primeros días de Aspose, sabíamos que ofrecer a nuestros clientes buenos productos no sería suficiente. También necesitábamos ofrecer un buen servicio. Nosotros mismos somos desarrolladores y entendemos lo frustrante que es cuando un problema técnico o una peculiaridad en el software le impide hacer lo que necesita hacer. Estamos aquí para resolver problemas, no para crearlos.

Es por eso que ofrecemos soporte gratuito. Cualquiera que utilice nuestro producto, ya sea que lo haya comprado o esté utilizando una evaluación, merece toda nuestra atención y respeto.



Puede registrar cualquier problema o sugerencia relacionada con Aspose.Cells Java para PHP utilizando cualquiera de las siguientes plataformas:


- 
[Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/issues)


### 
Ampliar y contribuir



Aspose.PDF Java para PHP es de código abierto y su código fuente está disponible en los principales sitios web de codificación social que se enumeran a continuación. Se anima a los desarrolladores a descargar el código fuente y contribuir sugiriendo o añadiendo nuevas funciones o mejorando las existentes, para que otros también puedan beneficiarse de él.

### Código fuente



Puede obtener el código fuente más reciente en una de las siguientes ubicaciones


- 
[Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)
