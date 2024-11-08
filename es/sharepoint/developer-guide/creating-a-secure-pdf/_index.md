---

title: Crear un PDF Seguro en SharePoint

linktitle: Creación de un PDF Seguro

type: docs

weight: 60

url: /es/sharepoint/creating-a-secure-pdf/

lastmod: "2020-12-16"

description: Usando la API de PDF SharePoint, puede producir PDFs seguros y encriptados y especificar sus contraseñas en SharePoint.

---



{{% alert color="primary" %}}



Aspose.PDF para SharePoint admite la creación de PDFs seguros. Instalar Aspose.PDF para SharePoint agrega una opción de **Configuración Segura de PDF** en la Configuración del Sitio. Aquí, puede establecer la contraseña de usuario, la contraseña del propietario y cualquier valor de la lista de algoritmos para encriptar el PDF de salida. La lista de algoritmos proporciona diferentes combinaciones de algoritmos de encriptación y tamaños de clave. Pase el valor de su elección.



Este artículo demuestra cómo usar Aspose.PDF para SharePoint para generar un PDF encriptado.



{{% /alert %}}



## **Creación de un PDF Seguro**



Para demostrar la característica, primero configuramos la opción de **Configuración Segura de PDF** para la contraseña del propietario y del usuario y el algoritmo de encriptación. El ejemplo luego fusiona dos documentos de una biblioteca de documentos.

### **Configuración de Opciones de Seguridad PDF**

Abre la opción de **Configuración de Seguridad PDF** desde la Configuración del Sitio y establece el algoritmo, contraseña del propietario y contraseña del usuario.

Especifica diferentes contraseñas de usuario y propietario al encriptar el archivo PDF.

- La contraseña de usuario, si se establece, es lo que necesitas proporcionar para abrir un PDF. Acrobat Reader solicita al usuario que ingrese la contraseña de usuario. Si es incorrecta, el documento no se abre.

- La contraseña del propietario, si se establece, controla permisos como impresión, edición, extracción, comentarios, etc. Acrobat Reader desactiva estas funciones basándose en la configuración de permisos. Acrobat requiere esta contraseña si deseas establecer/cambiar permisos.

![todo:image_alt_text](creating-a-secure-pdf_1.png)

### **Fusionar Documentos**

Fusiona dos documentos usando la opción de **Convertir a PDF**. Esta función fusiona varios archivos no PDF (HTML, texto o imagen) en un archivo PDF.

1. Abre una biblioteca de documentos y selecciona los documentos deseados de la lista.

![todo:image_alt_text](creating-a-secure-pdf_2.png)

1. Usa la opción **Combinar en PDF** de Herramientas de Biblioteca para guardar el archivo de salida. Se te pedirá que guardes el archivo de salida en el disco.

![todo:image_alt_text](creating-a-secure-pdf_3.png)

### **Salida**

El archivo de salida está encriptado.

![todo:image_alt_text](creating-a-secure-pdf_4.png)