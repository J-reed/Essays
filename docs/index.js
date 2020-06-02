

var lang = "Lang.ENGLISH";

var blog_directory = "/Essays/blogs/English/";

function setDefaultLang(){
    lang = "Lang.ENGLISH";
}

function setLang(){

    lang = document.getElementById("language_dropbox").value;

    switch(lang){
        case "Lang.ENGLISH":
            blog_directory = "/Essays/blogs/English/";
            break;
        case "Lang.FRENCH":
            blog_directory = "/Essays/blogs/French/";
            break;
        default:
            blog_directory = "/Essays/blogs/English/";
    }

}


function getBlogLink(blog_name){

    window.open(blog_directory + blog_name, "_self","", false);


}