# revision 22113
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-exa
# catalog-date 2011-04-14 19:55:22 +0200
# catalog-license lppl
# catalog-version 0.01
Name:		texlive-pst-exa
Version:	0.01
Release:	4
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
%{_texmfdistdir}/tex/latex/pst-exa/pst-exa.sty
%doc %{_texmfdistdir}/doc/latex/pst-exa/Changes
%doc %{_texmfdistdir}/doc/latex/pst-exa/README
%doc %{_texmfdistdir}/doc/latex/pst-exa/pst-exa-doc.pdf
%doc %{_texmfdistdir}/doc/latex/pst-exa/pst-exa-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.01-2
+ Revision: 755270
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.01-1
+ Revision: 719348
- texlive-pst-exa
- texlive-pst-exa
- texlive-pst-exa
- texlive-pst-exa

