Name:		texlive-pst-exa
Version:	0.06
Release:	2
Summary:	Typeset PSTricks examples, with code
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-exa
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-exa.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-exa.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The (PSTricks-related) package provides an environment
PSTexample to put code and output side by side or one above the
other.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pst-exa
%doc %{_texmfdistdir}/doc/latex/pst-exa

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
