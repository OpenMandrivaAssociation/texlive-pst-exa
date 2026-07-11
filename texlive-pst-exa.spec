%global tl_name pst-exa
%global tl_revision 45289

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.06
Release:	%{tl_revision}.1
Summary:	Typeset PSTricks examples, with code
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-exa
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-exa.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-exa.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The (PSTricks-related) package provides an environment PSTexample to put
code and output side by side or one above the other.

