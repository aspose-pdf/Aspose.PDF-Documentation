---
title: Descargar y Configurar Aspose.PDF en PHP
linktitle: Descargar y Configurar Aspose.PDF en PHP
type: docs
weight: 10
url: /es/java/download-and-configure-aspose-pdf-in-php/
description: Aprende cómo descargar y configurar Aspose.PDF en PHP para una fácil integración y manipulación de PDF dentro de tus proyectos PHP.
lastmod: "2026-09-03"
---
## Descargar Bibliotecas Requeridas

Descarga las bibliotecas requeridas mencionadas a continuación. Estas son las necesarias para ejecutar los ejemplos de Aspose.PDF Java for PHP.

- **Aspose:** [Aspose.PDF for Java Componente](https://downloads.aspose.com/pdf/java)
- PHP/Java Puente

## Descargar Ejemplos de Sitios de Codificación Social

Las siguientes versiones de ejemplos en funcionamiento están disponibles para descargar en los sitios de código social mencionados a continuación:

### GitHub

- **Aspose.PDF Java for PHP Ejemplos**
  - [Aspose.PDF Java for PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)

## Cómo configurar el código fuente en la plataforma Linux

Por favor, siga estos pasos simplesВ para abrir y ampliar el código fuente mientras usa:

## 1. Instalar el servidor Tomcat

Para instalar el servidor Tomcat, ejecute el siguiente comando en la consola de Linux.В Esto instalará correctamente el servidor Tomcat.

{{< highlight actionscript3 >}}

 sudo apt-get install tomcat8

{{< /highlight >}}

## 2. Descargar y Configurar PHP/JavaBridge

Para descargar los binarios de PHP/JavaBridge, ejecute el siguiente comando en la consola de Linux.

{{< highlight actionscript3 >}}

  wget http://citylan.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

Descomprima los binarios de PHP/JavaBridge ejecutando el siguiente comando en la consola de Linux.

{{< highlight actionscript3 >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

Esto extraeráВ **JavaBridge.war**В archivo. Cópialo al tomcat88В **webapps**В carpeta mediante el siguiente comando en la consola de Linux.

{{< highlight actionscript3 >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war

{{< /highlight >}}

Al copiar, tomcat8 creará automáticamente una nueva carpeta "**JavaBridge**" enВ **webapps**. Una vez que la carpeta se haya creado, asegúrese de que su tomcat8 esté ejecutándose y luego verifiqueВ  http://localhost:8080/JavaBridge В en el navegador, debería abrir una página predeterminada de JavaBridge.

Si aparece algún mensaje de error, entonces instalaВ **FastCGI**В ejecutando el siguiente comando en la consola de Linux.

{{< highlight actionscript3 >}}

  sudo apt-get install php55-cgi

{{< /highlight >}}

Después de instalar php5.5 CGI, reinicie el servidor tomcat8 y verifiqueВ  http://localhost:8080/JavaBridge В de nuevo en el navegador.

SiВ **JAVA_HOME**В error se muestra, entonces abra el archivo /etc/default/tomcat8 y descomente la línea que establece el JAVA_HOME. VerifiqueВ http://localhost:8080/JavaBridge В en el navegador de nuevo, debería aparecer con la página de ejemplos de PHP/JavaBridge.

## 3. Configurar ejemplos de Aspose.PDF Java para PHP

Clonar, ejemplos PHP ejecutando los siguientes comandos dentro de la carpeta webapps/JavaBridge.

{{< highlight actionscript3 >}}

$ git init&nbsp;

$ git clone [https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose.PDF-for-Java_for_PHP]

{{< /highlight >}}

## Cómo configurar el código fuente en Windows

Por favor siga los siguientes pasos simples para configurar PHP/Java Bridge en la plataforma Windows

1. Instale PHP5 y configúrelo como lo hace normalmente
2. Instale JRE 6 (Entorno de ejecución de Java) si aún no lo tiene. Puede comprobar esto en C:\Program Files etc. Puede descargarlo aquí . Estoy usando JRE 6 ya que es compatible con PHP Java Bridge (PJB).

3. Instale Apache Tomcat 8.0. Puede descargarlo aquí

4. Descargue JavaBridge.war.
5. Copie este archivo al directorio webapps de tomcat.
(ej: C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps )

6. Reinicie el servicio apache de tomcat.

7. Ir a  http://localhost:8080/JavaBridge/test.php  para comprobar si php funciona. Puedes encontrar otros ejemplos allí

8. Copie su [Aspose.PDF Java](https://downloads.aspose.com/pdf/java) archivo jar a C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib

9. Clonar [Aspose.PDF Java for PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP) ejemplos dentro de la carpeta C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\.

10. Copie la carpeta C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java a su carpeta de ejemplos de Aspose.PDF Java para PHP.

11. Reinicie el servicio de Apache Tomcat y comience a usar los ejemplos.
