---
title: Descargar y configurar Aspose.PDF en PHP
linktitle: Descargar y configurar Aspose.PDF en PHP
type: docs
weight: 10
url: /java/download-and-configure-aspose-pdf-in-php/
description: Aprenda a descargar y configurar Aspose.PDF en PHP para una fácil integración y manipulación de PDF dentro de sus proyectos PHP.
lastmod: "2026-06-09"
---
## 
Descargar bibliotecas requeridas



Descargue las bibliotecas requeridas que se mencionan a continuación. Estos son los ejemplos necesarios para ejecutar Aspose.PDF Java para PHP.

- **Aspose:** [Aspose.PDF para componente Java](https://downloads.aspose.com/pdf/java)

- Puente PHP/Java


## 
Descargar ejemplos de sitios de codificación social



Las siguientes versiones de ejemplos en ejecución están disponibles para descargar en los sitios de codificación social que se mencionan a continuación:


### 
GitHub

- **Aspose.PDF Ejemplos de Java para PHP**

  - [Aspose.PDF Java para PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)


## 
Cómo configurar el código fuente en la plataforma Linux



Siga estos sencillos pasos para abrir y ampliar el código fuente mientras usa:


## 1. Instale el servidor Tomcat

Para instalar el servidor Tomcat, ejecute el siguiente comando en la consola de Linux. Esto instalará correctamente el servidor Tomcat.


{{< highlight actionscript3 >}}

 
sudo apt-get instalar tomcat8


{{< /highlight >}}

## 2. Descargue y configure PHP/JavaBridge



Para descargar los binarios de PHP/JavaBridge, ejecute el siguiente comando en la consola de Linux.


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


Al copiar, Tomcat8 creará automáticamente una nueva carpeta "**JavaBridge**" en **webapps**. Una vez creada la carpeta, asegúrese de que su Tomcat8 se esté ejecutando y luego marque http://localhost:8080/JavaBridge В en el navegador, debería abrir una página predeterminada de JavaBridge.

Si aparece algún mensaje de error, instale **FastCGI**В emitiendo el siguiente comando en la consola de Linux.


{{< highlight actionscript3 >}}

  
sudo apt-get instalar php55-cgi


{{< /highlight >}}


Después de instalar php5.5 CGI, reinicie el servidor Tomcat8 y verifique http://localhost:8080/JavaBridge В nuevamente en el navegador.



Si se muestra el error **JAVA_HOME**В, abra el archivo /etc/default/tomcat8 y descomente la línea que establece JAVA_HOME. Marque В http://localhost:8080/JavaBridge В en el navegador nuevamente, debería venir con la página de ejemplos de PHP/JavaBridge.


## 3. Configurar Aspose.PDF Java para ejemplos de PHP

Clone ejemplos de PHP emitiendo los siguientes comandos dentro de la carpeta webapps/JavaBridge.


{{< highlight actionscript3 >}}


$ git init



$ git clon [https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose.PDF-for-Java_for_PHP]


{{< /highlight >}}

## 
Cómo configurar el código fuente en Windows



Siga los sencillos pasos a continuación para configurar PHP/Java Bridge en la plataforma Windows

1. Instale PHP5 y configúrelo como lo hace normalmente

2. Instale JRE 6 (Java Runtime Environment) si aún no lo tiene. Puede verificar esto en C:\Program Archivos, etc. Puede descargarlo aquí. Estoy usando JRE 6 porque es compatible con PHP Java Bridge (PJB).


3. Instale Apache Tomcat 8.0. Puedes descargarlo aquí


4. Descargue JavaBridge.war.

5. Copie este archivo al directorio de aplicaciones web de Tomcat.
(por ejemplo: C:\Program Archivos\Apache Software Foundation\Tomcat 8.0\webapps)


6. Reinicie el servicio Tomcat Apache.


7. Vaya a http://localhost:8080/JavaBridge/test.php para comprobar si php funciona. Puedes encontrar otros ejemplos allí.


8. Copie su archivo jar [Aspose.PDF Java](https://downloads.aspose.com/pdf/java) a C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib


9. Clonar ejemplos de [Aspose.PDF Java para PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP) dentro de la carpeta C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\.

10. Copie la carpeta C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java a su carpeta de ejemplos Aspose.PDF Java para PHP.


11. Reinicie el servicio Apache Tomcat y comience a usar ejemplos.
