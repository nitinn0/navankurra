import { useEffect, useMemo, useState } from 'react';
import { FiSearch } from 'react-icons/fi';
import CourseCard from '../components/courses/CourseCard.jsx';
import SectionTitle from '../components/ui/SectionTitle.jsx';
import useDebounce from '../hooks/useDebounce.js';
import { courses as courseData } from '../data/courses.js';

const categories = ['All', 'Web Development', 'Data Science', 'Cloud'];
const durations = ['All', '3 Months', '4 Months', '5 Months', '6 Months'];
const modeOptions = ['All', 'Online Live', 'Offline'];
const priceOptions = ['All', 'Under 30K', '30K-40K', 'Above 40K'];

export default function Courses() {
  const [search, setSearch] = useState('');
  const [category, setCategory] = useState('All');
  const [duration, setDuration] = useState('All');
  const [mode, setMode] = useState('All');
  const [price, setPrice] = useState('All');
  const [sort, setSort] = useState('Newest');
  const [page, setPage] = useState(1);
  const debouncedSearch = useDebounce(search, 350);

  const filteredCourses = useMemo(() => {
    return courseData
      .filter((course) => course.title.toLowerCase().includes(debouncedSearch.toLowerCase()))
      .filter((course) => (category === 'All' ? true : course.title.includes(category) || course.type.includes(category)))
      .filter((course) => (duration === 'All' ? true : course.duration === duration))
      .filter((course) => (mode === 'All' ? true : course.mode === mode))
      .filter((course) => {
        if (price === 'All') return true;
        if (price === 'Under 30K') return course.price < 30000;
        if (price === '30K-40K') return course.price >= 30000 && course.price <= 40000;
        return course.price > 40000;
      })
      .sort((a, b) => {
        if (sort === 'Lowest price') return a.price - b.price;
        if (sort === 'Highest price') return b.price - a.price;
        return a.title.localeCompare(b.title);
      });
  }, [category, debouncedSearch, duration, mode, price, sort]);

  const totalPages = Math.max(1, Math.ceil(filteredCourses.length / 6));
  const visibleCourses = filteredCourses.slice((page - 1) * 6, page * 6);

  useEffect(() => {
    setPage(1);
  }, [debouncedSearch, category, duration, mode, price, sort]);

  return (
    <section className="py-20">
      <div className="mx-auto max-w-7xl px-6 lg:px-8">
        <SectionTitle eyebrow="Courses" title="Find the right program for your goals" description="Filter by category, duration, pricing, and delivery model to discover the best fit." />

        <div className="mt-12 grid gap-8 lg:grid-cols-[1.2fr_0.8fr]">
          <div className="space-y-8">
            <div className="rounded-[32px] bg-white p-6 shadow-soft">
              <div className="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
                <div className="relative flex-1">
                  <FiSearch className="pointer-events-none absolute left-4 top-1/2 h-5 w-5 -translate-y-1/2 text-slate-400" />
                  <input
                    type="search"
                    value={search}
                    onChange={(e) => setSearch(e.target.value)}
                    placeholder="Search course title or keyword"
                    className="w-full rounded-3xl border border-slate-200 bg-slate-50 px-12 py-4 text-sm text-slate-800 outline-none transition focus:border-primary"
                  />
                </div>
                <select className="rounded-3xl border border-slate-200 bg-white px-4 py-4 text-sm text-slate-700 outline-none" value={sort} onChange={(e) => setSort(e.target.value)}>
                  <option>Newest</option>
                  <option>Lowest price</option>
                  <option>Highest price</option>
                </select>
              </div>

              <div className="mt-8 grid gap-4 sm:grid-cols-2 xl:grid-cols-4">
                <select className="rounded-3xl border border-slate-200 bg-slate-50 px-4 py-4 text-sm text-slate-700 outline-none" value={category} onChange={(e) => setCategory(e.target.value)}>
                  {categories.map((item) => (
                    <option key={item}>{item}</option>
                  ))}
                </select>
                <select className="rounded-3xl border border-slate-200 bg-slate-50 px-4 py-4 text-sm text-slate-700 outline-none" value={duration} onChange={(e) => setDuration(e.target.value)}>
                  {durations.map((item) => (
                    <option key={item}>{item}</option>
                  ))}
                </select>
                <select className="rounded-3xl border border-slate-200 bg-slate-50 px-4 py-4 text-sm text-slate-700 outline-none" value={mode} onChange={(e) => setMode(e.target.value)}>
                  {modeOptions.map((item) => (
                    <option key={item}>{item}</option>
                  ))}
                </select>
                <select className="rounded-3xl border border-slate-200 bg-slate-50 px-4 py-4 text-sm text-slate-700 outline-none" value={price} onChange={(e) => setPrice(e.target.value)}>
                  {priceOptions.map((item) => (
                    <option key={item}>{item}</option>
                  ))}
                </select>
              </div>
            </div>

            <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-3">
              {visibleCourses.map((course) => (
                <CourseCard key={course.id} course={course} />
              ))}
            </div>

            <div className="flex flex-wrap items-center justify-between gap-3 rounded-3xl bg-white p-6 shadow-soft">
              <p className="text-sm text-slate-600">Showing {visibleCourses.length} of {filteredCourses.length} courses</p>
              <div className="flex flex-wrap items-center gap-2">
                {Array.from({ length: totalPages }, (_, index) => (
                  <button
                    key={index + 1}
                    className={`rounded-full px-4 py-2 text-sm font-semibold transition ${page === index + 1 ? 'bg-primary text-white' : 'bg-slate-100 text-slate-700 hover:bg-slate-200'}`}
                    onClick={() => setPage(index + 1)}
                  >
                    {index + 1}
                  </button>
                ))}
              </div>
            </div>
          </div>

          <aside className="space-y-6 rounded-[32px] bg-white p-6 shadow-soft">
            <div className="rounded-[28px] bg-primary px-6 py-8 text-white shadow-lg">
              <p className="text-sm uppercase tracking-[0.28em] text-white/80">Need guidance?</p>
              <h3 className="mt-4 text-2xl font-semibold">Book a free consultation</h3>
              <p className="mt-4 text-sm leading-7 text-white/90">Talk to our admissions team and choose the option that fits you.</p>
              <a href="/contact" className="mt-6 inline-flex rounded-full bg-white px-5 py-3 text-sm font-semibold text-slate-950 transition hover:bg-slate-100">Contact us</a>
            </div>
            <div className="space-y-4 rounded-[28px] border border-slate-200 bg-slate-50 p-6">
              <p className="text-sm uppercase tracking-[0.3em] text-slate-500">Why learners choose us</p>
              <ul className="space-y-3 text-slate-600">
                <li>Expert-led training</li>
                <li>Live project portfolio</li>
                <li>One-on-one review</li>
              </ul>
            </div>
          </aside>
        </div>
      </div>
    </section>
  );
}
