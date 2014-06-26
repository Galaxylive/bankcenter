/*
 * ---------------------------------------------------------------- 
 *  Cufon font-replacement settings
 * ----------------------------------------------------------------  
 */

function cufon() {
	Cufon('.nav', {hover: {color: '#d16f4e'} });  //Navigation hover color
	Cufon('.title', {color: '#444', hover: {color: '#d16f4e'} }); //Blog and Portfolio item titles normal state (#444) and hover (#d16f4e) color
	Cufon('.home_tagline h1 a', {color: '#d16f4e', hover: {color: '#444'} }); //Home Tagline normal state and hover color
	Cufon('h1,h2,h3,h4,.home_tagline h1,.tagline h1,.over span,.bold,.dropcap1,.dropcap2,.nivo-caption', {hover: 'true'}); //Font replacement for all other elements
}		
cufon();