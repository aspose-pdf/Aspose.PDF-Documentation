---
title: Descargar y Configurar Aspose.PDF en PHP
type: docs
weight: 10
url: /es/java/download-and-configure-aspose-pdf-in-php/
lastmod: "2021-06-05"
---

## Descargar Bibliotecas Requeridas

Descargue las bibliotecas requeridas mencionadas a continuación. Estas son necesarias para ejecutar ejemplos de Aspose.PDF Java para PHP.

- **Aspose:** [Aspose.PDF para Componente Java](https://downloads.aspose.com/pdf/java)
- PHP/Java Bridge

## Descargar Ejemplos de Sitios de Codificación Social

Las siguientes versiones de ejemplos en ejecución están disponibles para descargar en los sitios de codificación social mencionados a continuación:

### GitHub

- **Ejemplos de Aspose.PDF Java para PHP**
  - [Aspose.PDF Java para PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)

## Cómo configurar el código fuente en la Plataforma Linux

Por favor siga estos simples pasos para abrir y extender el código fuente mientras usa:

## 1. Instalar el Servidor Tomcat

Para instalar el servidor Tomcat, emita el siguiente comando en la consola de Linux. Esto instalará exitosamente el servidor Tomcat.

{{< highlight actionscript3 >}}

 sudo apt-get install tomcat8

{{< /highlight >}}

## 2. Descargar y Configurar PHP/JavaBridge

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
 Una vez que la carpeta esté creada, asegúrate de que tu tomcat8 esté corriendo y luego verifica http://localhost:8080/JavaBridge en el navegador, debería abrir una página predeterminada de JavaBridge.

Si aparece algún mensaje de error, entonces instala **FastCGI** ejecutando el siguiente comando en la consola de Linux.

{{< highlight actionscript3 >}}

  sudo apt-get install php55-cgi

{{< /highlight >}}

Después de instalar php5.5 CGI, reinicia el servidor tomcat8 y verifica de nuevo http://localhost:8080/JavaBridge en el navegador.

Si se muestra el error **JAVA_HOME**, entonces abre el archivo /etc/default/tomcat8 y descomenta la línea que establece el JAVA_HOME. Verifica de nuevo http://localhost:8080/JavaBridge en el navegador, debería venir con la página de ejemplos de PHP/JavaBridge.

## 3. Configurar Aspose.PDF Java para ejemplos PHP

Clona los ejemplos de PHP emitiendo los siguientes comandos dentro de la carpeta webapps/JavaBridge.

{{< highlight actionscript3 >}}

$ git init&nbsp;


$ git clone [https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose.PDF-for-Java_for_PHP]
{{< /highlight >}}

## Cómo configurar el código fuente en Windows

Por favor, siga los siguientes pasos simples para configurar PHP/Java Bridge en la plataforma Windows

1. Instale PHP5 y configure como lo hace normalmente.
2. Instale JRE 6 (Entorno de Ejecución de Java) si no lo tiene ya. Puede verificar esto en C:\Program Files, etc. Puede descargarlo aquí. Estoy usando JRE 6 ya que es compatible con PHP Java Bridge (PJB).

3. Instale Apache Tomcat 8.0. Puede descargarlo aquí.

4. Descargue JavaBridge.war.
5. Copie este archivo en el directorio webapps de tomcat.
(ej: C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps)

6. Reinicie el servicio apache tomcat.

7. Vaya a http://localhost:8080/JavaBridge/test.php para verificar si PHP funciona. Puede encontrar otros ejemplos allí.

8. Copie su archivo jar de [Aspose.PDF Java](https://downloads.aspose.com/pdf/java) en C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib

9. Clona los ejemplos de [Aspose.PDF Java for PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP) dentro de la carpeta C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\.

10. Copia la carpeta C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java a tu carpeta de ejemplos de Aspose.PDF Java for PHP.

11. Reinicia el servicio de Apache Tomcat y comienza a usar los ejemplos.