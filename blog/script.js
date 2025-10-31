const articles = [
	{
		id: 1,
		title: 'Septimus Heap Book One: Magyk',
		date: 'July 5, 2022',
		description:
			'If you enjoy stories about seventh sons of seventh sons and magyk this is the book for you.',
		imgSrc: 'https://upload.wikimedia.org/wikipedia/en/5/5f/Magkycover2.jpg',
		imgAlt: 'Book cover for Septimus Heap 1',
		ages: '10-14',
		genre: 'Fantasy',
		stars: '⭐⭐⭐⭐',
        star_count: "4 out of 5 stars"
	},
	{
		id: 2,
		title: 'Magnus Chase Book One: Sword of Summer',
		date: 'December 12, 2021',
		description:
			'The anticipated new novel by Rick Riordan. After Greek mythology (Percy Jackson), Greek/Roman (Heroes of Olympus), and Egyptian (Kane Chronicles), Rick decides to try his hand with Norse Mythology, and the end result is good.',
		imgSrc:
			'https://books.google.com/books/content/images/frontcover/xWuyBAAAQBAJ?fife=w300',
		imgAlt: 'Book cover for Magnus Chase 1',
		ages: '12-16',
		genre: 'Fantasy',
		stars: '⭐⭐⭐⭐',
        star_count: "4 out of 5 stars"
	},
	{
		id: 3,
		title: "Belgariad Book One: Pawn of Prophecy",
		date: "Feb 12, 2022",
		description:
		"A fierce dispute among the Gods and the theft of a powerful Orb leaves the World divided into five kingdoms. Young Garion, with his 'Aunt Pol' and an elderly man calling himself Wolf --a father and daughter granted near-immortality by one of the Gods -- set out on a complex mission.",
		imgSrc:
		"https://images-na.ssl-images-amazon.com/images/I/41ZxXA+nInL.jpg",
		imgAlt: "Book cover for Pawn of Prophecy",
		ages: "12-16",
		genre: "Fantasy",
		stars: "⭐⭐⭐⭐⭐",
        star_count: "5 out of 5 stars"
	}
];
                
    articles.forEach(article => {
        // Code for going through each movie and creating content for that movie

        const articleSummary = `
 
        <section class="book-info">
            <li><em>${article.date}</em></li>
            <li>1${article.ages}</li>
            <li>${article.genre}</li>
            <li><span aria-label="${article.star_count}"></span>${article.stars}</li>
        </section>

        <section class="book-review">
            <h2>${article.title}</h2>
            <img src="${article.imgSrc}" alt="${article.imgAlt}">
            <p>${article.description}</p>
        </section>

        `;

        // adds the generated HTML to the page.
        document.getElementById("blog-post").innerHTML += articleSummary;
    });

// Github isn't hosting this script for some reason?
// ?? Something went wrong on their end. Rebuilding pages fixed it.