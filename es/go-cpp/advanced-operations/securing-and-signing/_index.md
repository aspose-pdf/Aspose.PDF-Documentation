---
title: Asegurando y firmando PDF en Go
linktitle: Asegurando y firmando PDF
type: docs
weight: 50
url: /es/go-cpp/securing-and-signing/
description: Esta sección describe las características de usar una firma y asegurar su documento PDF usando Go
lastmod: "2026-07-04"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Esta sección ofrece una guía completa para trabajar con documentos PDF seguros usando Aspose.PDF for Go via C++. Explica cómo proteger los archivos PDF con contraseñas, gestionar los permisos de acceso y abrir o desbloquear de forma segura documentos cifrados en aplicaciones Go.

El artículo recorre tareas comunes relacionadas con la seguridad de PDF, incluyendo el cifrado de PDFs con algoritmos criptográficos modernos, el descifrado de archivos protegidos con contraseña y el control del acceso de usuarios mediante banderas de permisos. También aprenderá cómo inspeccionar la configuración de permisos existente y abrir documentos seguros utilizando las credenciales del propietario para su procesamiento posterior.

Aprenderá cómo crear documentos PDF, aplicar protección criptográfica moderna usando cifrado basado en AES y controlar las capacidades del usuario, como imprimir, editar contenido y rellenar formularios. El artículo también muestra cómo abrir PDFs protegidos con contraseña utilizando credenciales de propietario y descifrarlos para producir documentos sin restricciones adecuados para su procesamiento posterior.

- [Cifrar y archivo PDF](/pdf/es/go-cpp/encrypt-pdf/)
- [Descifrar archivo PDF](/pdf/es/go-cpp/decrypt-pdf/)
- [Obtener permisos](/pdf/es/go-cpp/get-permissions/)
- [Establecer permisos](/pdf/es/go-cpp/set_permissions/)
- [Abrir un PDF protegido con contraseña](/pdf/es/go-cpp/open-password-protected-pdf/)

Para trabajar con Set Permissions y Get Permissions, consulte la tabla PDF Permissions Reference. Que enumera los indicadores de permiso disponibles que pueden aplicarse a un documento PDF para controlar cómo los usuarios finales interactúan con él.

## Referencia de permisos de PDF

| **Permiso** | **Descripción** |
| :- | :- |
| PrintDocument | Permitir imprimir |
| ModifyContent | Permitir modificar contenido (excepto forms/annotations) |
| ExtractContent | Permitir copiar/extraer texto y gráficos |
| ModifyTextAnnotations | Permitir agregar/modificar anotaciones de texto |
| FillForm | Permitir rellenar formularios interactivos |
| ExtractContentWithDisabilities | Permitir la extracción de contenido para accesibilidad |
| AssembleDocument | Permitir insertar/rotar/eliminar páginas o cambiar la estructura |
| PrintingQuality | Permitir impresión de alta calidad / fiel |


