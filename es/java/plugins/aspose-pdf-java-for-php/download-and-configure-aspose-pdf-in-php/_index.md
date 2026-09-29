---
title: Descargar y configurar Aspose.PDF en PHP
linktitle: Descargar y configurar Aspose.PDF en PHP
type: docs
weight: 10
url: /es/java/download-and-configure-aspose-pdf-in-php/
description: Aprenda cómo descargar y configurar Aspose.PDF en PHP para una integración fácil y manipulación de PDF dentro de sus proyectos PHP.
lastmod: "2026-09-29"
---
## Descargar bibliotecas requeridas

Descargue las bibliotecas requeridas mencionadas a continuación. Estas son las requeridas para ejecutar los ejemplos de Aspose.PDF Java para PHP.

- **Aspose:** [Componente Aspose.PDF for Java](https://downloads.aspose.com/pdf/java)
- Puente PHP/Java

## Descargar ejemplos de sitios de codificación social

Las siguientes versiones de ejemplos en ejecución están disponibles para descargar en los sitios de codificación social mencionados a continuación:

### GitHub

- **Aspose.PDF Java for PHP Ejemplos**
  - [Aspose.PDF Java for PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)

## Configurar el código fuente en la plataforma Linux

Por favor, siga estos simples pasos para abrir y ampliar el código fuente mientras usa:

## 1. Instalar el servidor Tomcat

Para instalar el servidor Tomcat, ejecute el siguiente comando en la consola de Linux. Esto instalará correctamente el servidor Tomcat.

{{< highlight actionscript3 >}}

 sudo apt-get install tomcat8

{{< /highlight >}}

## 2. Descargar y configurar PHP/JavaBridge

Para descargar los binarios de PHP/JavaBridge, ejecute el siguiente comando en la consola de Linux.

{{< highlight actionscript3 >}}

  wget http://citylan.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

Descomprima los binarios de PHP/JavaBridge ejecutando el siguiente comando en la consola de Linux.

{{< highlight actionscript3 >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

Esto extraerá **JavaBridge.war** archivo. Copia lo al tomcat88 **webapps** directorio ejecutando el siguiente comando en la consola de Linux.

{{< highlight actionscript3 >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war

{{< /highlight >}}

Al copiar, tomcat8 creará automáticamente una nueva directorio "**JavaBridge**" in **webapps**. Una vez creada la directorio, asegúrese de que su tomcat8 esté ejecutándose y luego verifique  http://localhost:8080/JavaBridge  en el navegador, debería abrir una página predeterminada de JavaBridge.

Si aparece algún mensaje de error, entonces instala  **FastCGI** ejecutando el siguiente comando en la consola de Linux.

{{< highlight actionscript3 >}}

  sudo apt-get install php55-cgi

{{< /highlight >}}

Después de instalar php5.5 CGI, reinicie el servidor tomcat8 y verifique  http://localhost:8080/JavaBridge  de nuevo en el navegador.

Si **JAVA_HOME** se muestra el error, entonces abra el archivo /etc/default/tomcat8 y descomente la línea que establece el JAVA_HOME. Verifique\u0412 http://localhost:8080/JavaBridge  en el navegador de nuevo, debería venir con la página de ejemplos de PHP/JavaBridge.

## 3. Configure Aspose.PDF Java for PHP Examples

Clonar, ejemplos PHP mediante la ejecución de los siguientes comandos dentro de la directorio webapps/JavaBridge.

{{< highlight actionscript3 >}}

$ git init&nbsp;

$ git clone [https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose.PDF-for-Java_for_PHP]

{{< /highlight >}}

## Configurar el código fuente en Windows

Por favor, siga los siguientes pasos simples para configurar PHP/Java Bridge en la plataforma Windows.

1. Instale PHP5 y configúrelo como lo hace normalmente.
2. Instale JRE 6 (Java Runtime Environment) si aún no lo tiene. Puede verificar esto en C:\Program Files, etc. Puede descargarlo aquí. Estoy usando JRE 6 ya que es compatible con PHP Java Bridge (PJB).

3. Instale Apache Tomcat 8.0. Puede descargarlo aquí.

4. Descargue JavaBridge.war.
5. Copie este archivo al directorio webapps de tomcat.
(ej: C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps )

6. Reinicie el servicio Apache Tomcat.

7. Vaya a  http://localhost:8080/JavaBridge/test.php  para comprobar si php funciona. Puede encontrar otros ejemplos allí.

8. Copie su [Aspose.PDF Java](https://downloads.aspose.com/pdf/java) archivo jar a C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib.

9. Clone [Aspose.PDF Java for PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP) ejemplos dentro de la directorio C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\.

10. Copie la directorio C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java a la directorio de ejemplos de Aspose.PDF Java for PHP.

11. Reinicie el servicio de Apache Tomcat y comience a usar los ejemplos.
