interface BlogIndexPage {
    id: number;
    title: string;
    intro: string;  
}

interface BlogPage {
    id: number;
    meta: {
      slug: string;
    };
    title: string;
    date: string;
    intro: string;
}

export default async function BlogIndex() {
    // Fetch the BlogIndexPage's details
    const indexPages = await fetch(
        `http://localhost:8000/api/v2/pages/?${new URLSearchParams({
          type: "blog.BlogIndexPage",
          slug: "blog",
          fields: "intro",
    })}`, {
        headers: {
            Accept: "application/json",
        },
    }
    ).then((response) => response.json());

    // there's only one with the slug "blog"
    const index: BlogIndexPage = indexPages.items[0];

    //Fetch the blogpages that are children of the BlogIndexPage instace

    const data = await fetch(
        `http://127.0.0.1:8000/api/v2/pages/?${new URLSearchParams({
          type: "blog.BlogPage",
          child_of: index.id.toString(),
          fields: ["date", "intro"].join(","),
        })}`,
        {
          headers: {
            Accept: "application/json",
          },
        }
    ).then((response) => response.json());

      // Use BlogPage instances as the posts
    const posts: BlogPage[] = data.items;

    return (
      <main>
        <div className="mb-8">
          <h1 className="text-4xl font-bold mb-2">Blog</h1>
          <div><p>Some introduction</p></div>
        </div>
        <ul>
          {posts.map((child) => (
            <li key={child.id} className="mb-4">
              <a className="underline" href={`blog/${child.meta.slug}`}>
                <h2>{child.title}</h2>
              </a>
              <time dateTime={child.date}>
                {new Date(child.date).toDateString()}
              </time>
              <p>{child.intro}</p>
            </li>
          ))}
        </ul>
      </main>
    );
  }