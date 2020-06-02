var Lang = {
    ENGLISH: 0,
    FRENCH: 1,
};

var lang = Lang.ENGLISH;

var blog_directory = "/Essays/blogs/English/";

function setDefaultLang(){
    lang = Lang.ENGLISH;
}

function setLang(){

    lang = document.getElementById("language_dropbox").value;

    switch(lang){
        case 0:
            blog_directory = "/Essays/blogs/English/";
            break;
        case 1:
            blog_directory = "/Essays/blogs/French/";
            break;
        default:
            blog_directory = "/Essays/blogs/English/";
    }

}


function getBlogLink(blog_name){

    window.open(blog_directory + blog_name, "_self","", false);


}