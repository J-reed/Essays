var Lang = {
    ENGLISH: 0,
    FRENCH: 1,
};

var lang = Lang.ENGLISH;

var blog_directory = "/Essays/blogs/English/";

function setDefaultLang(){
    lang = Lang.ENGLISH;
}

function setLang(new_lang){

    switch(new_lang){
        case 0:
            lang = Lang.ENGLISH;
            blog_directory = "/Essays/blogs/English/";
            break;
        case 1:
            lang = Lang.FRENCH;
            blog_directory = "/Essays/blogs/French/";
            break;
        default:
            lang = Lang.ENGLISH;
            blog_directory = "/Essays/blogs/English/";
    }

}


function getBlogLink(blog_name){

    window.open(blog_directory + blog_name, _blank,replace= true);


}