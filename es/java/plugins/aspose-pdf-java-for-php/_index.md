---
title: Aspose.PDF Java para PHP
linktitle: Aspose.PDF Java para PHP
type: docs
weight: 50
url: /es/java/aspose-pdf-java-for-php/
description: Aprenda cómo integrar Aspose.PDF for Java en proyectos PHP. Desbloquee funcionalidades avanzadas de PDF para sus aplicaciones web.
lastmod: "2026-09-03"
---
## Introducción a Aspose.PDF Java para PHP

### Puente PHP / Java

El PHP/Java Bridge es una implementación de un streaming, basado en XML\u0412 [protocolo de red](http://php-java-bridge.sourceforge.net/pjb/PROTOCOL.TXT), que puede usarse para conectar un motor de scripts nativo, por ejemplo PHP, Scheme o Python, con una máquina virtual Java. Es hasta 50 veces más rápido que RPC local vía SOAP, requiere menos recursos en el lado del servidor web. Es\u0412 [más rápido](http://php-java-bridge.sourceforge.net/pjb/FAQ.html#performance)В y más fiable que la comunicación directa mediante la Java Native Interface, y no requiere componentes adicionales para invocar procedimientos Java desde PHP o procedimientos PHP desde Java.

Leer más en [sourceforge.net](http://php-java-bridge.sourceforge.net/pjb/)

### Aspose.PDF for Java

Aspose.PDF for Java es un componente de creación de documentos PDF que permite a sus aplicaciones Java leer, escribir y manipular documentos PDF sin utilizar Adobe Acrobat.

Aspose.PDF for Java es un componente de precio asequible que ofrece una increíble cantidad de funciones, que incluyen: opciones de compresión de PDF, creación y manipulación de tablas, soporte de gráficos, funciones de imagen, funcionalidad extensa de hipervínculos, controles de seguridad ampliados y manejo de fuentes personalizadas.

Aspose.PDF for Java le permite crear archivos PDF directamente a través de la API proporcionada y plantillas XML. Usar Aspose.PDF for Java también le habilitará para agregar capacidades PDF a sus aplicaciones en poco tiempo.

### Aspose.PDF Java para PHP

El proyecto Aspose.PDF para PHP muestra cómo se pueden realizar diferentes tareas usando las API de Aspose.PDF Java en PHP. Este proyecto está dirigido a proporcionar ejemplos útiles para desarrolladores PHP que desean utilizar Aspose.PDF para Java en sus proyectos PHP usando [PHP/Java Bridge](http://php-java-bridge.sourceforge.net/pjb/).

## Requisitos del sistema y plataformas compatibles

### Requisitos del sistema

A continuación se presentan los requisitos del sistema para usar Aspose.PDF for PHP via Java:

- Servidor Tomcat 8.0 o superior instalado.
- PHP/JavaBridge está configurado.
- FastCGI está instalado.
- Componente Aspose.PDF descargado.

### Plataformas compatibles

A continuación se presentan las plataformas compatibles:

- PHP 5.3 o superior
- Java 1.8 o superior

## Descargas y Configurar

### Descargar Bibliotecas Requeridas

Descargue las bibliotecas requeridas mencionadas a continuación. Estas son las necesarias para ejecutar ejemplos de Aspose.PDF Java para PHP.

- **Aspose:** [Aspose.PDF for Java Componente](https://downloads.aspose.com/pdf/java)
- PHP/Java Bridge

### Descargar ejemplos de sitios de codificación social

Las siguientes versiones de ejemplos en funcionamiento están disponibles para descargar en los sitios de codificación social mencionados a continuación:

### GitHub

- Ejemplos de Aspose.PDF Java para PHP
  - [Aspose.PDF Java para PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)

### Cómo configurar el código fuente en la plataforma Linux

Por favor, siga estos pasos simplesВ para abrir y ampliar el código fuente mientras se usa:

### 1. Instalar Tomcat Server

Para instalar el servidor tomcat, ejecute el siguiente comando en la consola de Linux.В Esto instalará correctamente el servidor tomcat.

{{< highlight actionscript3 >}}

 sudo apt-get install tomcat8

{{< /highlight >}}

### 2. Descargar y Configurar PHP/JavaBridge

Para descargar los binarios de PHP/JavaBridge, ejecute el siguiente comando en la consola de linux.

{{< highlight actionscript3 >}}

  wget http://citylan.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

Descomprime los binarios de PHP/JavaBridge ejecutando el siguiente comando en la consola de Linux.

{{< highlight actionscript3 >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

Esto extraeráВ **JavaBridge.war**В archivo. Cópialo a tomcat88В **webapps**В carpeta ejecutando el siguiente comando en la consola de Linux.

{{< highlight actionscript3 >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war

{{< /highlight >}}

Al copiar, tomcat8 creará automáticamente una nueva carpeta "**JavaBridge**" en **webapps**.

Si aparece algún mensaje de error, entonces instale **FastCGI** ejecutando el siguiente comando en la consola de Linux.

{{< highlight actionscript3 >}}

  sudo apt-get install php55-cgi

{{< /highlight >}}

Si se muestra un error **JAVA_HOME**, entonces abra el archivo /etc/default/tomcat8 y descomente la línea que establece JAVA_HOME.

### 3. Configurar ejemplos de Aspose.PDF Java para PHP

Clonar, ejemplos PHP ejecutando los siguientes comandos dentro de la carpeta webapps/JavaBridge.В

{{< highlight actionscript3 >}}

$ git init&nbsp;

$ git clone [https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose.PDF-for-Java_for_PHP]

{{< /highlight >}}

### Cómo configurar el código fuente en la plataforma Windows

Por favor, siga los siguientes pasos simples para configurar PHP/Java Bridge en la plataforma Windows

1. Instale PHP5 y configúrelo como normalmente lo hace
2. Instale JRE 6 (Java Runtime Environment) si usted donвЂ™t ya lo tiene. Puede verificar esto en C:\Program Files etc. Puede descargarlo aquí . Estoy usando JRE 6 ya que es compatible con PHP Java Bridge (PJB).

3. Instala Apache Tomcat 8.0. Puedes descargarlo aquí

4. Descargar [JavaBridge.war](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/JavaBridgeTemplate621.war/download). Copia este archivo al directorio webapps de tomcat.
(ej: C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps )

5. Reinicie el servicio tomcat apache.

6. Ir a http://localhost:8080/JavaBridge/test.php para comprobar si php funciona. Puedes encontrar otros ejemplos allí

7. Copie su [Aspose.PDF Java](https://downloads.aspose.com/pdf/java) archivo jar a C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib

8. Clonar [Aspose.PDF Java para PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP) ejemplos dentro C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\ folder.

9. Copie la carpeta C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java a su carpeta de ejemplos de Aspose.PDF Java para PHP.

10. Reinicie el servicio apache tomcat y comience a usar los ejemplos.

## Soporte, Extender y Contribuir

### Soporte

Desde los primeros días de Aspose, supimos que simplemente ofrecer a nuestros clientes buenos productos no sería suficiente. También necesitábamos brindar un buen servicio. Somos desarrolladores nosotros mismos y entendemos lo frustrante que es cuando un problema técnico o una peculiaridad del software te impide hacer lo que necesitas hacer. Estamos aquí para resolver problemas, no crearlos.

Por eso ofrecemos soporte gratuito. Cualquier usuario de nuestro producto, ya sea que lo haya comprado o lo esté evaluando, merece toda nuestra atención y respeto.

Puedes registrar cualquier problema o sugerencia relacionado con\u0412\u00A0Aspose.Cells Java for PHP usando cualquiera de las siguientes plataformas:

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/issues)

### Extender y Contribuir

Aspose.PDF Java for PHP es de código abierto y su código fuente está disponible en los principales sitios web de codificación social que se enumeran a continuación. Se anima a los desarrolladores a descargar el código fuente y contribuir sugiriendo o añadiendo nuevas funcionalidades o mejorando las existentes, de modo que otros también puedan beneficiarse de ello.

### Código fuente

Puede obtener el código fuente más reciente de una de las siguientes ubicaciones

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)
