const handleRecipeSearch = async (e) => {
  e.preventDefault();
  $("#spinner").show();
  const ingredients = $("#ingredients-input").val();
  const { data } = await axios.post("/recipes", { ingredients: ingredients });
  if (typeof data === "object") {
    homepageRecipesMarkup(data);
  } else {
    document.body.innerHTML = data;
  }
};

$("#search-recipe-form").on("submit", handleRecipeSearch);

const homepageRecipesMarkup = (data) => {
  $("#homepage").removeClass("homepage");
  $("#homepageRecipes").empty();
  $("#spinner").hide();
  if (data.results.length === 0) {
    const results = $(
      "<div class='text-white mb-5 mx-3' >No results found. Please try again.</div>"
    );
    results.appendTo($("#homepageRecipes"));
  } else {
    for (recipe of data.results) {
      const divCard = $("<div class='card mb-5 mx-3'></div>");

      const recipeMarkup = $(
        `<div class="row no-gutters"> <div class="col-md-4"> <img src=${recipe.image} class="card-img"/></div><div class="col-md-8"><div class="card-body"><h5 class="card-title"><a href="/recipe/${recipe.id}">${recipe.title}</a><span class="badge badge-secondary" style="margin-left: 10px">&#9829; ${recipe.aggregateLikes}</span></h5></div></div></div><div class="text-center"><ul class="list-group list-group-flush"><li class="list-group-item">${recipe.usedIngredientCount} Used Ingredients</li><li class="list-group-item">Calories: ${recipe.nutrition.nutrients[0].amount} kcal</li><li class="list-group-item"><div class="d-flex flex-row justify-content-center flex-wrap" id="dietDiv-${recipe.id}"></div></li><li class="list-group-item"><div class="d-flex flex-row justify-content-center flex-wrap" id="cuisineDiv-${recipe.id}"></div></li></ul>
        </div>`
      );
      recipeMarkup.appendTo(divCard);

      if (recipe.diets.length === 0) {
        $(recipeMarkup[1].children[0].children[2].children[0]).append(
          $("<span>N/A</span>")
        );
      }
      for (d of recipe.diets) {
        const markup = `<span class="badge badge-pill badge-info mx-2 my-1">${d}</span>`;
        $(recipeMarkup[1].children[0].children[2].children[0]).append(markup);
      }

      if (recipe.cuisines.length === 0) {
        $(recipeMarkup[1].children[0].children[3].children[0]).append(
          $("<span>N/A</span>")
        );
      }
      for (c of recipe.cuisines) {
        const markup = `<span class="badge badge-pill badge-success mx-2 my-1">${c}</span>`;
        $(recipeMarkup[1].children[0].children[3].children[0]).append(markup);
      }

      divCard.appendTo($("#homepageRecipes"));
    }
  }
};

const handleRecipeSave = async (e) => {
  e.preventDefault();
  if ($(e.target).hasClass("fa-regular")) {
    await axios.post(`/recipe/${e.target.dataset.recipeId}/save`);
    $(e.target).removeClass("fa-regular");
    $(e.target).addClass("fa-solid");
  } else {
    await axios.post(`/recipe/${e.target.dataset.recipeId}/unsave`);
    $(e.target).removeClass("fa-solid");
    $(e.target).addClass("fa-regular");
  }
};

$("#save-icon").on("click", handleRecipeSave);
